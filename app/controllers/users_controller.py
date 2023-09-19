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
    