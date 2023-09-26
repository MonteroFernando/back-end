from flask import request
from ..models.messages_model import Message
from datetime import datetime
class MessageController:
    @classmethod
    def create(cls):
        data=request.json
        if not 'content' in data:
            return {'error':'Se debe ingresar el contenido del mensaje'},400
        message=Message(**data)
        Message.create(message)
        return {'mensaje':'mensaje creado con éxito'},200
    
    @classmethod
    def get(cls):
        id=request.args.get('id',None)
        id_users=request.args.get('id_users',None)
        id_channels=request.args.get('id_channels',None)
        created=request.args.get('created',None)
        if not id and not id_users and not id_channels and not created:
            message_obj=None
        else:
            try:
                created=datetime.strptime(created,'%Y-%m-%d %H:%M:%S')
            except ValueError:
                return {'error':'created no cumple el formato esperado: yyyy-mm-dd hh:mm:ss'},400
            except TypeError:
                created=None
            message_obj=Message(id=id,id_users=id_users,id_channels=id_channels,created=created)
        messages=Message.get(message_obj)
        if messages ==[]:
            return {'mensaje':'No se encontraron datos en la consulta'},400
        for m in messages:
            m.created=datetime.strftime(m.created,'%Y-%m-%d %H:%M:%S')
        return [message.serialize() for message in messages]
    
    @classmethod
    def update(cls):
        data=request.json
        if not 'id' in data:
            return {'error':'No se recibio el id del mensaje a modificar'},400
        message=Message(**data)
        if message.created:
            try:
                message.created=datetime.strptime(message.created,'%Y-%m-%d %H:%M:%S')
            except ValueError:
                return {'error':'created no cumple con el formato esperado: yyyy-mm-dd hh:mm:ss'},400
        Message.update(message)
        return {'mensaje':'mensaje actualizado con éxito'},200
    
    @classmethod
    def delete(cls,id):
        Message.delete(id)
        return {'mensaje':'Mensaje eliminado con éxito'},200

    




    

