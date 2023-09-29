from ..database import DatabaseConnection

class Server:
    _keys=('id','name','description','img','user_id','category_id')

    def __init__(self,**kwargs):
        self.id=kwargs.get('id')
        self.name=kwargs.get('name')
        self.description=kwargs.get('description')
        self.img=kwargs.get('img')
        self.category_id=kwargs.get('category_id')
    
    def serialize(self):
        return self.__dict__
    
    @classmethod
    def create(cls,server):
        query="INSERT INTO teamhub.servers (name,description,img,category_id) VALUES(%s,%s,%s,%s)"
        params=(server.name,server.description,server.img,server.category_id)
        DatabaseConnection.execute_query(query,params)
    
    @classmethod
    def get(cls,server=None):
        if not server:
            query="SELECT * FROM teamhub.servers"
            servers=DatabaseConnection.fetchall(query)

        else:
            data=vars(server)
            keys=list("{}=%s".format(key) for key,val in data.items() if val)
            query=f"SELECT * FROM teamhub.servers WHERE {keys[0]}"
            params=tuple(val for val in data.values() if val)
            servers=DatabaseConnection.fetchall(query,params)
        return [cls(**dict(zip(cls._keys,row))) for row in servers]
    @classmethod
    def update(cls,data):
        keys=' ,'.join("{}=%s".format (key) for key in data.keys() if key != 'id')
        query=f"UPDATE teamhub.servers SET {keys} WHERE id=%s"
        params=tuple(param for k,param in data.items() if k != 'id')+(data['id'],)
        DatabaseConnection.execute_query(query,params)
    @classmethod
    def delete(cls,id):
        query="DELETE FROM teamhub.servers WHERE id=%s"
        params=(id,)
        DatabaseConnection.execute_query(query,params)
    @classmethod
    def lastid(cls):
        query="SELECT max(id) from teamhub.servers"
        lid=DatabaseConnection.fetchone(query)
        return lid
        

        