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

    @classmethod
    def get(cls):
        user_id=request.args.get('user_id', None)
        server_id=request.args.get('server_id',None)
        member_obj=Member(user_id=user_id,server_id=server_id)
        members=Member.get(member_obj)
        return [member.serialize() for member in members],200
    
    @classmethod
    def update(cls):
        data=request.json
        if not 'id' in data:
            return {'error':'No se ingreso el id a modificar'},400
        if not 'server_id' in data and not 'user_id' in data:
            return {'error':'Por lo menos se debe pasar un dato a modificar'},400
        Member.update(data)
        return {'mensaje':'Member modificado con éxito'},200
    
    @classmethod
    def delete(cls,id):
        Member.delete(id)
        return {'mensaje':'Member elimimado con éxito'}
    
        
    
    
        