from ..models.servers_model import Server
from flask import request

class ServerController:
    @classmethod
    def create(cls):
        data=request.json
        if not 'name' in data:
            return {'error':'No se ingresaron todos los campos obligatorios'},400
        server=Server(**data)
        Server.create(server)
        id=Server.lastid()
        return {'mensaje':'Servidor creado con éxito','id':id},200
    @classmethod
    def get(cls):
        id=request.args.get('id',None)
        name=request.args.get('name',None)
        category_id=request.args.get('category_id',None)
        if not id and not name and not category_id:
            server=None
        else:
            server=Server(id=id,name=name,category_id=category_id)
        response=Server.get(server)
        if response is None:
            return {'mensaje':'No se encontraron datos'}
        else:
            return [server.serialize() for server in response],200
    @classmethod
    def update(cls):
        data=request.json
        if not 'id' in list(data):
            return {'error':'No se ingreso el Id a modificar'},400
        Server.update(data)
        return {'mensaje':'Usuario modificado con éxito'},200
    @classmethod
    def delete(cls,id=None):
        if not id:
            return{'error':'No se ingreso el id a eliminar'},400
        
        Server.delete(id)
        return {'mensaje':'Usuario eliminado con éxito'},200
    

        
        
    