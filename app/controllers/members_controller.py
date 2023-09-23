from ..models.members_model import Member
from flask import request

class MemeberController:
    @classmethod
    def create(cls):
        data=request.json
        if not 'user_id' in data or not 'server_id' in data:
            return {'mensaje':'Se deben ingresar todos los datos necesarios'},400
        member=Member(**data)
        Member.create(member)
        return {'mensaje':'Members creado con éxito'},200
    def get_all(cls):
        data=request.json
        members=Member.get_all(data)
        return [member.serialize() for member in members]
    
        