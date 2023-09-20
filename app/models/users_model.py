from ..database import DatabaseConnection

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
        return self.__dict__
    
    @classmethod
    def create(cls,user):
        """Crea un nuevo usuario
        Args:
        -user(user):objeto user"""
        query="""INSERT INTO teamhub.users (username, password, email, img, firstname, lastname) VALUES (%s,%s,%s,%s,%s,%s)"""
        params=(user.username,user.password,user.email,user.img,user.firstname,user.lastname)
        DatabaseConnection.execute_query(query,params)
    
    @classmethod
    def get_all(cls):
        """Devuelve todos los usuarios"""
        query="""SELECT * FROM teamhub.users"""
        response=DatabaseConnection.fetchall(query)
        return [cls(**dict(zip(cls._keys, row))) for row in response]

    @classmethod
    def get(cls,data):
        """Devuelve el usuario con el dato ingresado como parametro, solo de los datos unicos.
        Args:
            data (dict): Diccionario con una sola key. Admitidos: id,username,email"""
        key=''.join("{}=%s".format(key) for key in data.keys())
        query=f'SELECT id,username,password,email,img,firstname,lastname FROM teamhub.users WHERE {key}'
        params=tuple(data.values())
        response=DatabaseConnection.fetchone(query,params)
        return cls(**dict(zip(cls._keys, response)))
        
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
    def update(cls,data):
        """Elimina el id recibido en el diccionario del parametro.
        Args:
        data(dict): diccionario, de 1 solo elemento con el id del usuario"""
        query = 'DELETE FROM teamhub.users WHERE users.id=%s'
        params = (data['id'],)
        DatabaseConnection.execute_query(query,params)


        






        
