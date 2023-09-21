from ..database import DatabaseConnection

class Server:
    _keys=('id','name','description','img','user_id','category_id')

    def __init__(self,**kwargs):
        self.id=kwargs.get('id')
        self.name=kwargs.get('name')
        self.description=kwargs.get('description')
        self.img=kwargs.get('img')
        self.user_id=kwargs.get('user_id')
        self.category_id=kwargs.get('category_id')
    
    def serialize(self):
        return self.__dict__
    
    @classmethod
    def create(cls,server):
        query="INSERT INTO teamhub.servers (name,description,img,user_id,category_id) VALUES(%s,%s,%s,%s,%s)"
        params=(server.name,server.description,server.img,server.user_id,server.category_id)
        DatabaseConnection.execute_query(query,params)
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM teamhub.servers"
        servers=DatabaseConnection.fetchall(query)
        return [cls(**dict(zip(cls._keys,row))) for row in servers]
    @classmethod
    def get(cls,data):
        keys=''.join("{}=%s".format(key) for key in data.keys())
        query=f"SELECT * FROM teamhub.servers WHERE {keys}"
        params=tuple(data.values())
        response=DatabaseConnection.fetchone(query,params)
        if response is None:
            return None
        else:
            return cls(**dict(zip(cls._keys,response)))
    @classmethod
    def update(cls,data):
        keys=' ,'.join("{}=%s".format (key) for key in data.keys() if key != 'id')
        query=f"UPDATE teamhub.servers SET {keys} WHERE id=%s"
        params=tuple(param for k,param in data.items() if k != 'id')+(data['id'],)
        DatabaseConnection.execute_query(query,params)
    @classmethod
    def delete(cls,data):
        query="DELETE FROM teamhub.servers WHERE id=%s"
        params=(data['id'],)
        DatabaseConnection.execute_query(query,params)
        

        