from ..database import DatabaseConnection

class Category:
    _keys=('id','name','img')
    def __init__(self,**kwargs):
        self.id=kwargs.get('id')
        self.name=kwargs.get('name')
        self.img=kwargs.get('img')
    
    def serialize(self):
        return self.__dict__
    
    @classmethod
    def create(cls,data):
        query="""INSERT INTO teamhub.categories (name,img) VALUES (%s,%s)"""
        params=(data.name,data.img)
        DatabaseConnection.execute_query(query,params)
    
    @classmethod
    def get(cls,data):
        key=' ,'.join("{}=%s".format(key) for key in data.keys())
        query=f"SELECT * FROM teamhub.categories WHERE {key}"
        params=tuple(data.values())
        response=DatabaseConnection.fetchone(query,params)
        return cls(**dict(zip(cls._keys,response)))
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM teamhub.categories"
        response=DatabaseConnection.fetchall(query)
        return [cls(**dict(zip(cls._keys,row))) for row in response]
    
    @classmethod
    def update(cls,data):
        key=' ,'.join("{}=%s".format (key) for key in data.keys() if key!='id')
        query=f"UPDATE teamhub.categories SET {key} WHERE id=%s"
        params=tuple(value for k,value in data.items() if k!='id')+(data['id'],)
        DatabaseConnection.execute_query(query,params)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM teamhub.categories WHERE id=%s'
        params = (data['id'],)
        DatabaseConnection.execute_query(query,params)





