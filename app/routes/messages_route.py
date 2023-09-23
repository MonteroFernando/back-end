from flask import Blueprint
from ..controllers.messages_controller import MessageController

message_bp=Blueprint('messabe_bp',__name__)

message_bp.route('/create', methods=['POST'])(MessageController.create)
message_bp.route('/get', methods=['GET'])(MessageController.get)