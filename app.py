from flask import Flask, request
from flask_cors import CORS
from base import Base
import json
from io import BytesIO

import random

from draw import draw_cover
from vk_utils import update_cover
from base64 import encodebytes, decodebytes

app = Flask(__name__)
CORS(app)
base = Base()


@app.route("/groups_list")
def group_list():
	user_id = request.args["uid"]

	group_list = base.get("%s:list" % user_id, default=[])

	covers = []
	for group_id in group_list:
		info = base.get("%s:%s:info" % (user_id, group_id), default=[])
		covers.append(info["render_cover"])	

	result = dict(zip(group_list, covers))
	
	return json.dumps(result), 200

@app.route("/group_info")
def group_info():
	user_id = request.args["uid"]
	group_id = request.args["gid"]

	info = base.get("%s:%s:info" % (user_id, group_id), default={})

	return json.dumps(info), 200


@app.route("/update_group", methods=["POST"])
def update_group():
	data = json.loads(request.data.decode("utf-8"))

	user_id = data["uid"]
	group_id = data["gid"]

	new_info = data["info"]
	old_info = base.get("%s:%s:info" % (user_id, group_id), default={})

	if type(new_info) is not dict: return  "", 400


	old_info = new_info
	if "render_cover" not in old_info["info"]:
		old_info["info"]["render_cover"] = old_info["info"]["cover"]["background"].decode()

	group_list = base.get("%s:list" % user_id, default=[])
	base.set("%s:%s:info" % (user_id, group_id), old_info)

	group_list = base.get("%s:list" % user_id, default=[])
	if group_id not in group_list: group_list.append(group_id)
	base.set("%s:list" % user_id, group_list)


	full_groups_list = base.get("group-list", default=[])
	if "%s:%s" % (user_id, group_id) not in full_groups_list: full_groups_list.append("%s:%s" % (user_id, group_id))
	base.set("group-list", full_groups_list)


	return "", 200




@app.route("/")
def index():
	return "Hello world", 200


@app.route("/update")
def update_heads():
	groups_list = base.get("group-list", default=[])

	for gid in groups_list:
		info = base.get("%s:info" % gid, default={})

		cover = draw_cover(info["cover"], random.randint(1,2000))


		img = BytesIO()
		cover.save(img, format="png")
		img.seek(0)

		info["render_cover"] = encodebytes(img.getvalue()).decode()
		base.set("%s:info" % gid, info)

		update_cover(gid.split(":")[1], info["token"], img)


	return "",200

if __name__ == "__main__":
	app.run()