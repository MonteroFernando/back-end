from flask import request
from ..models.messages_model import Message

class MessageController:
    @classmethod
    def create(cls):
        data=request.json
        if not 'content' in data:
            return {'error':'Se debe ingresar el contenido del mensaje'}
        message=Message(**data)
        Message.create(message)
        return {'mensaje':'mensaje creado con éxito'}
    
    @classmethod
    def get(cls):
        id=request.args.get('id',None)
        id_users=request.args.get('id_users',None)
        id_channels=request.args.get('id_channels',None)
        created=request.args.get('created',None)
        if not id and not id_users and not id_channels and not created:
            message_obj=None
        else:
            message_obj=Message(id=id,id_users=id_users,id_channels=id_channels,created=created)
        messages=Message.get(message_obj)
        if messages ==[]:
            return {'mensaje':'No se encontraron datos en la consulta'}
        return [message.serialize() for message in messages]


    

