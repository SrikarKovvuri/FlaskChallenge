from flask import Flask
from app.views.greeting import greet
from app.views.goodbye import bye
from app.views.errors import errors
from app.views.fun import fun
def create_app():

    app = Flask(__name__)

    app.register_blueprint(bye)
    app.register_blueprint(greet)
    app.register_blueprint(errors)
    app.register_blueprint(fun)
    
    return app

    