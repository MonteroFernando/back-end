from ..database import DatabaseConnection

class User:
    def __init__(self, id=None, username=None, password=None,email=None,img=None,firstname=None,lastname=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.img = img
        self.firstname = firstname
        self.lastname = lastname

    def serialize(self):
        return {
            "id":self.id,
            "username":self.username,
            "password":self.password,
            "email":self.email,
            "img":self.img,
            "firstname":self.firstname,
            "lastname":self.lastname
        }
    
    @classmethod
    def create(self,user):
        """Crea un nuevo usuario
        Args:
        -user(user):objeto user"""
        query="""INSERT INTO teamhub.users (username, password, email, img, firstname, lastname) VALUES (%s,%s,%s,%s,%s,%s)"""
        params=(user.username,user.password,user.email,user.img,user.firstname,user.lastname)
        DatabaseConnection.execute_query(query,params)
    
    @classmethod
    def get(self):
        """Devuelve todos los usuarios"""
        query="""SELECT * FROM teamhub.users"""
        responce=DatabaseConnection.fetchall(query)
        lista=[]
        for user in responce:
            usuario=User(id=user[0],
                         username=user[1],
                         password=user[2],
                         email=user[3],
                         img=user[4],
                         firstname=user[5],
                         lastname=user[6])
            lista.append(usuario.serialize())
        return {'users':lista}
