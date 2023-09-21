from flask import Blueprint

from ..controllers.users_controller import UserController

user_bp = Blueprint('user_bp',__name__)

user_bp.route('/create',methods=['POST'])(UserController.create)
user_bp.route('/get_all',methods=['GET'])(UserController.get_all)
user_bp.route('/get',methods=['GET'])(UserController.get)
user_bp.route('/update',methods=['PUT'])(UserController.update)
user_bp.route('/delete',methods=['DELETE'])(UserController.delete)
