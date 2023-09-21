from flask import Blueprint

from ..controllers.categories_controller import CategoryController

category_bp=Blueprint('category_bp',__name__)

category_bp.route('/create',methods=['POST'])(CategoryController.create)
category_bp.route('/get_all',methods=['GET'])(CategoryController.get_all)
category_bp.route('/get',methods=['GET'])(CategoryController.get)
category_bp.route('/update',methods=['PUT'])(CategoryController.update)
category_bp.route('/delete',methods=['DELETE'])(CategoryController.delete)
