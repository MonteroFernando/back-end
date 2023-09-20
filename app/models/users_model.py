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
        response=DatabaseConnection.fetchall(query)
        lista=[]
        for user in response:
            usuario=User(id=user[0],
                         username=user[1],
                         password=user[2],
                         email=user[3],
                         img=user[4],
                         firstname=user[5],
                         lastname=user[6])
            lista.append(usuario.serialize())
        return {'users':lista}

    @classmethod
    def get_one(self,data):
        """Devuelve el usuario con el dato ingresado como parametro, solo de los datos unicos.
        Args:
            data (dict): Diccionario con una sola key. Admitidos: id,username,email"""
        key=''.join("{}=%s".format(key) for key in data.keys())
        query=f'SELECT id,username,password,email,img,firstname,lastname FROM teamhub.users WHERE {key}'
        params=tuple(data.values())
        response=DatabaseConnection.fetchone(query,params)
        user_ob=User(
            id=response[0],
            username=response[1],
            password=response[2],
            email=response[3],
            img=response[4],
            firstname=response[5],
            lastname=response[6]
        )
        user=User.serialize(user_ob)
        return user
    
    @classmethod
    def update(self,data):
        """Metodo que modifica un usuario.
        parametro obligatorio del diccionario es id, luego los valores que se van a modificar.
        Args:
        data(dict): diccionario"""
        key=', '.join("{}=%s".format(key) for key in data.keys() if key!='id')
        query=f'UPDATE teamhub.users SET {key} WHERE users.id=%s'
        params= tuple(value for key,value in data.items() if key != "id")+(data["id"],)
        DatabaseConnection.execute_query(query,params)
        






        
