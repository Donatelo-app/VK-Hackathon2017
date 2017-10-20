from flask import Flask, request
from base import Base
import json

app = Flask(__name__)
base = Base


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


@app.route("/update_group")
def update_group():
	data = json.loads(request.data.decode("utf-8"))

	user_id = data["uid"]
	group_id = data["gid"]

	info = data["info"]

	base.set("%s:%s:info" % (user_id, group_id), info)

	return "", 200




@app.route("/")
def index():
	return "Hello world", 200


if __name__ == "__main__":
	app.run()