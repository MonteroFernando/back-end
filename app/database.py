import mysql.connector

class DatabaseConnection:
    _connection=None
    _config = None
    
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                user = cls._config['DATABASE_USERNAME'],
                password = cls._config['DATABASE_PASSWORD'],
                port = cls._config['DATABASE_PORT'],
                host = cls._config['DATABASE_HOST'],
            )
            
        return cls._connection
    
    @classmethod
    def set_config(cls,config):
        cls._config = config
    
    @classmethod
    def _execute_query(cls,query,params=None):
        """Metodo privado de clase que crear el cursor y ejecuta el query, 
        retornando el cursor con la consulta realizada"""
        cursor=cls.get_connection().cursor()
        cursor.execute(query,params)
        return cursor
    
    @classmethod
    def execute_query(cls,query,params=None):
        cursor=cls._execute_query(query,params)
        cls._connection.commit()
        return cursor
    
    @classmethod
    def fetchall(cls,query,params=None):
        cursor=cls._execute_query(query,params)
        return cursor.fetchall()

    @classmethod
    def fetchone(cls,query,params=None):
        cursor=cls._execute_query(query,params)
        return cursor.fetchone()
    
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None
