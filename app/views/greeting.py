from flask import Flask, Blueprint, jsonify, abort
from app.utils.errors import NotFoundError

greet = Blueprint("greet", __name__,url_prefix = "/greetings")

@greet.route("/hello", methods = ["GET"])
def hello():
    raise NotFoundError("404: Not Found")


@greet.route("/salut", methods = ["GET"])
def salut():
    return jsonify({"salut": True}), 200




