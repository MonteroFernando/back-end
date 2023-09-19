from flask import Blueprint

from ..controllers.users_controller import UserController

user_bp = Blueprint('user_bp',__name__)

user_bp.route('/create_user',methods=['POST'])(UserController.create)
user_bp.route('/',methods=['GET'])(UserController.get)
