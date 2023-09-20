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
    def create(cls,data):
        pass