from flask import Flask, Blueprint, jsonify
from app.utils.errors import Unauthorized

fun = Blueprint("fun", __name__, url_prefix = "/fun")

@fun.route("/vacation", methods = ["GET"])
def vacation():
    return jsonify({"vacation": True}), 200

@fun.route("/holiday", methods = ["GET"])
def holiday():
    raise Unauthorized("401: Unauthorized")

