from ..database import DatabaseConnection
from .members_model import Member
from .servers_model import Server

class User:
    _keys=('id','username','password','email','img','firstname','lastname')

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.email = kwargs.get('email')
        self.img = kwargs.get('img')
        self.firstname = kwargs.get('firstname')
        self.lastname = kwargs.get('lastname')

    def serialize(self):
        lista_servidor=[]
        members=Member.get(Member(user_id=self.id))
        for m in members:
            servers=Server.get(Server(id=m.server_id))
            for s in servers:
                lista_servidor.append(s.serialize())
        return {
            'id':self.id,
            'username':self.username,
            'password':self.password,
            'email':self.email,
            'img':self.img,
            'firstname':self.firstname,
            'lastname':self.lastname,
            'servers':lista_servidor

        }
    
    @classmethod
    def create(cls,user):
        """Crea un nuevo usuario
        Args:
        -user(user):objeto user"""
        query="""INSERT INTO teamhub.users (username, password, email, img, firstname, lastname) VALUES (%s,%s,%s,%s,%s,%s)"""
        params=(user.username,user.password,user.email,user.img,user.firstname,user.lastname)
        DatabaseConnection.execute_query(query,params)
        
    @classmethod
    def get(cls,user):
        """Devuelve el usuario con el dato ingresado como parametro.
        Args:
            user (User): Objeto User"""
        if not user:
            query="""SELECT * FROM teamhub.users"""
            response=DatabaseConnection.fetchall(query)
        else:
            data=vars(user)
            keys=''.join("{}=%s".format(key) for key,val in data.items() if val)
            #Esta linea esta para modificar a... keys = "{}=%s".format(list(data.keys())[0])
            #La dejo asi por ahora, en el caso de users no se usaria mas de una condición asi que estaria bien modificarla
            #para las otras tablas podriamos usar esto agregado AND u OR antes del .join, segun la necesidad.
            query=f'SELECT * FROM teamhub.users WHERE {keys}'
            params=tuple(val for val in data.values() if val)
            response=DatabaseConnection.fetchall(query,params)
        return [cls(**dict(zip(cls._keys, row))) for row in response]
        
    @classmethod
    def update(cls,data):
        """Metodo que modifica un usuario.
        parametro obligatorio del diccionario es id, luego los valores que se van a modificar.
        Args:
        data(dict): diccionario"""
        key=', '.join("{}=%s".format(key) for key in data.keys() if key!='id')
        query=f'UPDATE teamhub.users SET {key} WHERE users.id=%s'
        params= tuple(value for key,value in data.items() if key != "id")+(data["id"],)
        DatabaseConnection.execute_query(query,params)

    @classmethod
    def delete(cls,id):
        """Elimina el id recibido como parametro.
        Args:
        id(int): el id del user a eliminar"""
        query = 'DELETE FROM teamhub.users WHERE users.id=%s'
        params = (id,)
        DatabaseConnection.execute_query(query,params)



        






        
