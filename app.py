from flask import Flask, request
from flask_cors import CORS
from base import Base
import json

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


	for key in new_info:
		old_info[key] = new_info[key]


	group_list = base.get("%s:list" % user_id, default=[])
	base.set("%s:%s:info" % (user_id, group_id), old_info)

	group_list = base.get("%s:list" % user_id, default=[])
	if group_id not in group_list: group_list.append(group_id)
	base.set("%s:list" % user_id, group_list)

	return "", 200




@app.route("/")
def index():
	return "Hello world", 200


if __name__ == "__main__":
	app.run()