from flask import Flask, Blueprint, jsonify

bye = Blueprint("bye", __name__, url_prefix = "/goodbye")

@bye.route("/au_revoir", methods = ["GET"])
def au():
    return jsonify({"au_revoir": True}), 200

@bye.route("/see_ya", methods = ["GET"])
def see_ya():
    return jsonify({"see_ya": True}), 200