from flask import Blueprint
from ..controllers.members_controller import MemeberController

members_bp=Blueprint('members_bp',__name__)

members_bp.route('/create',methods=['POST'])(MemeberController.create)
