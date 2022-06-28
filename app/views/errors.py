from flask import Flask, Blueprint, jsonify, abort
from app.utils.errors import NotFoundError
from app.utils.errors import ForbiddenError
from app.utils.errors import Unauthorized

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(Exception)
def not_found(e):
    if(isinstance(e, NotFoundError)):
        return "404", 404

    if(isinstance(e, ForbiddenError)):
        return "403", 403

    if(isinstance(e, Unauthorized)):
        return "401", 401
    return "300", 300
