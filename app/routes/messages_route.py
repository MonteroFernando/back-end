from flask import Blueprint
from ..controllers.messages_controller import MessageController

message_bp=Blueprint('messabe_bp',__name__)

message_bp.route('/create', methods=['POST'])(MessageController.create)
message_bp.route('/get', methods=['GET'])(MessageController.get)
message_bp.route('/update',methods=['PUT'])(MessageController.update)
message_bp.route('/delete/<int:id>',methods=['DELETE'])(MessageController.delete)

