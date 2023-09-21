from ..database import DatabaseConnection

class Message:
    _keys=('id','id_users','id_channels','content','created')
    def __init__(self,**kwargs):
        self.id=kwargs.get('id')
        self.id_users=kwargs.get('id_users')
        self.id_server=kwargs.get('id_channels')
        self.content=kwargs.get('content')
        self.created=kwargs.get('created')
    @classmethod
    def create(cls,message):
        query="INSERT INTO teamhub.messages (id_users,id_channels,content,created) VALUES (%s,%s,%s,%s)"
        params=(message.id_users,message.id_server,message.content,message.created)
        DatabaseConnection.execute_query(query,params)
    @classmethod
    def get_all(cls,data=None):
        if data==None:
            query="SELECT * FROM teamhub.messages"
            response=DatabaseConnection.fetchall(query)
        elif len(data)>1:
            keys=' AND '.join('{}=%s'.format(key) for key in data.keys())
            query=f"SELECT * FROM teamhub.messages WHERE {keys}=%s ORDER BY created"
            params=tuple(data.values())
            response=DatabaseConnection.fetchall(query,params)
        else:
            keys='{}=%s'.format(list(data.keys())[0])
            query=f"SELECT * FROM teamhub.messages WHERE {keys}=%s ORDER BY created"
            params=tuple(data.values())
            response=DatabaseConnection.fetchall(query,params)
        return [cls(**dict(zip(cls._keys,row)))for row in response]
    @classmethod
    def get(cls,data):
        query="SELECT * FROM teamhub.messages WHERE is=%s"
        params=(data['id'],)
        response=DatabaseConnection.fetchone(query,params)
        return cls(**dict(zip(cls._keys,response)))
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
