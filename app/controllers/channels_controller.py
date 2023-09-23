from flask import request
from ..models.channels_model import Channel

class ChannelController:
    @classmethod
    def create(cls):
        data=request.json
        if not 'name' in data and not 'server_id' in data:
            return {'error': 'se deben ingresar todos los datos necesarios'}
        channel=Channel(**data)
        Channel.create(channel)
        return {'mensaje':'Channel creado con éxito'},200
    
    @classmethod
    def get(cls):
        name=request.args.get('name',None)
        id=request.args.get('id',None)
        if not name and not id:
            channel_obj=None
        else:
            channel_obj=Channel(name=name,id=id)
        channels=Channel.get_all(channel_obj)
        return [Channel.serialize(channel) for channel in channels]
    
    @classmethod
    def update(cls):
        data=request.json
        if not 'id' in data:
            return {'error':'No se ingreso el id al modificar'}
        Channel.update(data)
        return {'mensaje':'Channel actualizado con éxito'}
    @classmethod
    def delete(cls,id):
        channel_obj=Channel(id=id)
        Channel.delete(channel_obj)
        return {'mensaje':'Channel eliminado con éxito'}
    

    
    
    
