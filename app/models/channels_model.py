from ..database import DatabaseConnection

class Channel:
    _keys=('id','name','server_id')
    def __init__(self,**kwargs):
        self.id=kwargs.get('id')
        self.name=kwargs.get('name')
        self.server_id=kwargs.get('server_id')
    def serialize(self):
        return self.__dict__
    @classmethod
    def create(cls,channel):
        query="INSERT INTO teamhub.channels (name,server_id) VALUES (%s,%s)"
        params=(channel.name,channel.server_id)
        DatabaseConnection.execute_query(query,params)
    @classmethod
    def get(cls,channel=None):
        if not channel:
            query="SELECT * FROM teamhub.channels"
            response=DatabaseConnection.fetchall(query)
        else:
            data=vars(channel)
            keys=list(key for key,val in data.items() if val)
            query=f"SELECT * FROM teamhub.channels WHERE {keys[0]}=%s"
            params=tuple(val for val in data.values() if val )
            response=DatabaseConnection.fetchall(query,params)
        return [cls(**dict(zip(cls._keys,row)))for row in response]
    @classmethod
    def update(cls,data):
        keys=' ,'.join('{}=%s'.format(key) for key in data.keys() if key !='id')
        query=f"UPDATE teamhub.channels SET {keys} WHERE id=%s"
        params=tuple(value for k,value in data.items() if k != 'id')+(data['id'],)
        DatabaseConnection.execute_query(query,params)
    @classmethod
    def delete(cls,channel):
        query="DELETE FROM teamhub.channels WHERE id=%s"
        params=(channel.id,)
        DatabaseConnection.execute_query(query,params)
