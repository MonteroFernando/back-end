from ..database import DatabaseConnection

class Member:
    _keys=('id','user_id','server_id')
    def __init__(self,**kwargs):
        self.id=kwargs.get('id')
        self.user_id=kwargs.get('user_id')
        self.server_id=kwargs.get('server_id')

    def serialize(self):
        return self.__dict__
    
    @classmethod
    def create(cls,member):
        query="INSERT INTO teamhub.members (user_id,server_id) VALUES (%s,%s)"
        params=(member.user_id,member.server_id)
        DatabaseConnection.execute_query(query,params)
    @classmethod
    def get_all(cls,data=None):
        if data==None:
            query="SELECT * FROM teamhub.members"
            response=DatabaseConnection.fetchall(query)
        else:
            keys='{}=%s'.format(list(data.keys())[0])
            query=f"SELECT * FROM teamhub.members WHERE {keys}=%s"
            params=tuple(data.values())
            response=DatabaseConnection.fetchall(query,params)
        return [cls(**dict(zip(cls._keys,row)))for row in response]
    @classmethod
    def get(cls,data):
        query="SELECT * FROM teamhub.members WHERE id=%s"
        params=(data['id'],)
        response=DatabaseConnection.fetchone(query,params)
        return cls(**dict(zip(cls._keys,response)))
    @classmethod
    def update(cls,data):
        keys=' ,'.join('{}=%s'.format(key) for key in data.keys() if key !='id')
        query=f"UPDATE teamhub.members SET {keys} WHERE id=%s"
        params=tuple(value for k,value in data.items() if k != 'id')+(data['id'],)
        DatabaseConnection.execute_query(query,params)
    @classmethod
    def delete(cls,data):
        query="DELETE FROM teamhub.members WHERE id=%s"
        params=(data['id'],)
        DatabaseConnection.execute_query(query,params)
