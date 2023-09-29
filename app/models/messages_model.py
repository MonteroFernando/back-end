from ..database import DatabaseConnection

class Message:
    _keys=('id','id_users','id_channels','content','created','username')
    def __init__(self,**kwargs):
        self.id=kwargs.get('id')
        self.id_users=kwargs.get('id_users')
        self.id_channels=kwargs.get('id_channels')
        self.content=kwargs.get('content')
        self.created=kwargs.get('created')
        self.username=kwargs.get('username')
    def serialize(self):
        return self.__dict__
    @classmethod
    def create(cls,message):
        query="INSERT INTO teamhub.messages (id_users,id_channels,content) VALUES (%s,%s,%s)"
        params=(message.id_users,message.id_channels,message.content)
        DatabaseConnection.execute_query(query,params)
    @classmethod
    def get(cls,message):
        if not message:
            query="""SELECT messages.*,users.username FROM teamhub.messages JOIN teamhub.users
             ON teamhub.messages.id_users=teamhub.users.id ORDER BY created"""
            response=DatabaseConnection.fetchall(query)
        else:
            data=vars(message)
            if len([val for key,val in data.items() if val])>1:
                keys=' AND '.join('{}=%s'.format(key) for key,val in data.items() if val)
            else:
                keys=''.join('{}=%s'.format(key) for key,val in data.items() if val)
            query=f"""SELECT messages.*,users.username FROM teamhub.messages JOIN teamhub.users ON
             teamhub.messages.id_users=teamhub.users.id WHERE {keys} ORDER BY created"""
            params=tuple(val for k,val in data.items() if val)
            response=DatabaseConnection.fetchall(query,params)
        return [cls(**dict(zip(cls._keys,row)))for row in response]
    @classmethod
    def update(cls,message):
        data=vars(message)
        keys=' ,'.join('{}=%s'.format(key) for key,val in data.items() if key !='id' and val)
        query=f"UPDATE teamhub.messages SET {keys} WHERE id=%s"
        params=tuple(val for k,val in data.items() if k != 'id' and val)+(data['id'],)
        DatabaseConnection.execute_query(query,params)
    @classmethod
    def delete(cls,id):
        query="DELETE FROM teamhub.messages WHERE id=%s"
        params=(id,)
        DatabaseConnection.execute_query(query,params)
