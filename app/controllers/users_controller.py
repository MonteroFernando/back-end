from ..models.users_model import User

from flask import request

class UserController:
    """Controlador de la Clase User"""
    @classmethod
    def create(cls):
        data=request.json
        user=User(**data)
        User.create(user)
        return{'mensaje': 'Usuario creado con éxito'},200
    @classmethod
    def get(cls):
        users=User.get()
        return users,200
    @classmethod
    def get_one(cls):
        data=request.json
        permitted=('id','username','email')
        if len(data)> 1:
            return {'error':'Se han introdicido mas de un dato'},400
        if not list(data)[0] in permitted:
            return {'error':'Los datos ingresados no son permitidos'},400
        response=User.get_one(data)
        return response,200
    @classmethod
    def update(cls):
        data=request.json
        if not 'id' in list(data):
            return {'error':'No se ingreso el Id a modificar'},400
        User.update(data)
        return {'mensaje':'Usuario modificado con éxito'},200

        
        
    