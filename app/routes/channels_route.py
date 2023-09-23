from flask import Blueprint
from ..controllers.channels_controller import ChannelController

channel_bp=Blueprint('channel_bp', __name__)

channel_bp.route('/create', methods=['POST'])(ChannelController.create)
channel_bp.route('/get',methods=['GET'])(ChannelController.get)
channel_bp.route('/update',methods=['PUT'])(ChannelController.update)
channel_bp.route('/delete/<int:id>',methods=['DELETE'])(ChannelController.delete)



