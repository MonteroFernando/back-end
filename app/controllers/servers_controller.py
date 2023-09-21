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
        return {'mensaje':'Servidor creado con éxito'},200
    @classmethod
    def get_all(cls):
        servers=Server.get_all()
        return [server.serialize() for server in servers],200
    @classmethod
    def get(cls):
        data=request.json
        permitted=('id')#se podria poner name como unique para agregar aqui
        if len(data)> 1:
            return {'error':'Se han introducido mas de un dato'},400
        if not list(data)[0] in permitted:
            return {'error':'Los datos ingresados no son permitidos'},400
        response=Server.get(data)
        if response is None:
            return {'mensaje':'No se encontraron datos'}
        else:
            return response.serialize(),200
    @classmethod
    def update(cls):
        data=request.json
        if not 'id' in list(data):
            return {'error':'No se ingreso el Id a modificar'},400
        Server.update(data)
        return {'mensaje':'Usuario modificado con éxito'},200
    @classmethod
    def delete(cls):
        data=request.json
        if not 'id' in list(data):
            return{'error':'No se ingreso el id a eliminar'},400
        Server.delete(data)
        return {'mensaje':'Usuario eliminado con éxito'},200
    

        
        
    