from ..models.users_model import User
from flask import request

class UserController:
    """Controlador de la Clase User"""
    @classmethod
    def create(cls):
        data=request.json
        obligated={'username','email','password'}
        if not obligated.issubset(set(list(data))):
            return {'error':'No se ingresaron todos los campos obligatorios'},400
        user=User(**data)
        User.create(user)
        return{'mensaje': 'Usuario creado con éxito'},200
    @classmethod
    def get(cls):
        id=request.args.get('id',None)
        username=request.args.get('username',None)
        email=request.args.get('email',None)
        if not id and not username and not email:
            user=None
        else:
            user_obj=User(id=id,username=username,email=email)
        users=User.get(user_obj)
        return [user.serialize()for user in users],200
    @classmethod
    def update(cls):
        data=request.json
        if not 'id' in list(data):
            return {'error':'No se ingreso el Id a modificar'},400
        User.update(data)
        return {'mensaje':'Usuario modificado con éxito'},200
    @classmethod
    def delete(cls,id):
        User.delete(id)
        return {'mensaje':'Usuario eliminado con éxito'},200
    

        
        
    