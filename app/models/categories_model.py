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
        response=DatabaseConnection.execute_query(query,params)
        return cls(**dict(zip(cls._keys,response)))


