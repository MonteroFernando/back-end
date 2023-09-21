from flask import Blueprint
from ..controllers.servers_controller import ServerController

server_bp=Blueprint('server_bp',__name__)

server_bp.route('/create',methods=['POST'])(ServerController.create)
server_bp.route('/get_all',methods=['GET'])(ServerController.get_all)
server_bp.route('/get',methods=['GET'])(ServerController.get)
server_bp.route('/update',methods=['PUT'])(ServerController.update)
server_bp.route('/delete',methods=['DELETE'])(ServerController.delete)
