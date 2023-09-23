from ..database import DatabaseConnection

class Message:
    _keys=('id','id_users','id_channels','content','created')
    def __init__(self,**kwargs):
        self.id=kwargs.get('id')
        self.id_users=kwargs.get('id_users')
        self.id_server=kwargs.get('id_channels')
        self.content=kwargs.get('content')
        self.created=kwargs.get('created')
    def serialize(self):
        return self.__dict__
    @classmethod
    def create(cls,message):
        query="INSERT INTO teamhub.messages (id_users,id_channels,content) VALUES (%s,%s,%s)"
        params=(message.id_users,message.id_server,message.content)
        DatabaseConnection.execute_query(query,params)
    @classmethod
    def get(cls,message):
        if not message:
            query="SELECT * FROM teamhub.messages"
            response=DatabaseConnection.fetchall(query)
        else:
            data=vars(message)
            if len([val for key,val in data.items() if val])>1:
                keys=' AND '.join('{}=%s'.format(key) for key,val in data.items() if val)
            else:
                keys=''.join('{}=%s'.format(key) for key,val in data.items() if val)
            query=f"SELECT * FROM teamhub.messages WHERE {keys} ORDER BY created"
            params=tuple(val for k,val in data.items() if val)
            response=DatabaseConnection.fetchall(query,params)
        return [cls(**dict(zip(cls._keys,row)))for row in response]
    @classmethod
    def update(cls,data):
        keys=' ,'.join('{}=%s'.format(key) for key in data.keys() if key !='id')
        query=f"UPDATE teamhub.messages SET {keys} WHERE id=%s"
        params=tuple(value for k,value in data.items() if k != 'id')+(data['id'],)
        DatabaseConnection.execute_query(query,params)
    @classmethod
    def update(cls,data):
        query="DELETE FROM teamhub.messages WHERE id=%s"
        params=(data['id'])
        DatabaseConnection.execute_query(query,data)
