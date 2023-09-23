from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.user_route import user_bp
from .routes.categories_route import category_bp
from .routes.servers_route import server_bp
from .routes.members_route import member_bp
from .routes.channels_route import channel_bp

from .database import DatabaseConnection

def init_app():

    app=Flask(__name__,static_folder=None,template_folder=None)

    CORS(app,supports_credentials=True)

    app.config.from_object(Config)

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(user_bp,url_prefix='/users')
    app.register_blueprint(category_bp, url_prefix='/categories')
    app.register_blueprint(server_bp,url_prefix='/servers')
    app.register_blueprint(member_bp,url_prefix='/members')
    app.register_blueprint(channel_bp, url_prefix='/channels')

    return app