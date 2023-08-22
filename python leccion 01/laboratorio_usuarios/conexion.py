from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'public'
    _USERNAME = '' #rellenar
    _PASSWORD = '' #rellenar
    _DB_PORT = '' #rellenar
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE )
            except Exception as e:
                print(e)
                sys.exit()
        return cls._pool


    @classmethod
    def obtenerConexion(cls):
        con = cls.obtenerPool().getConn()
        return con


    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)


    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()


