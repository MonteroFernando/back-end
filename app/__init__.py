from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.bp import user_bp

from .database import DatabaseConnection

def init_app():

    app=Flask(__name__,static_folder=None,template_folder=None)

    CORS(app,supports_credentials=True)

    app.config.from_object(Config)

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(user_bp,url_prefix='/users')
    return app