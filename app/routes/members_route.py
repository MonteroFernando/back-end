from flask import Blueprint
from ..controllers.members_controller import MemeberController

member_bp=Blueprint('member_bp',__name__)

member_bp.route('/create',methods=['POST'])(MemeberController.create)
member_bp.route('/get_all',methods=['GET'])(MemeberController.get_all)
member_bp.route('/get',methods=['GET'])(MemeberController.get)
member_bp.route('/update', methods=['PUT'])(MemeberController.update)
member_bp.route('/delete', methods=['DELETE'])(MemeberController.delete)


