from cursor_del_pool import CursorDelPool
from usuario import Usuario
import sys

class UsuarioDao:
    _SELECCIONAR = "SELECT * FROM usuario ORDER BY id_persona"
    _INSERTAR = "INSERT INTO usuario(username, password) VALUES(%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s"
    _ELIMINAR = "DELETE FROM usuario WHERE id_usuario=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            try:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                

                # Se puede así
                #usuarios = list(map(lambda registro: Usuario(registro[0], registro[1], registro[2]), registros))
                #y así
                usuarios = [Usuario(registro[0], registro[1], registro[2]) for registro in registros]
                #o así
                #usuarios = (lambda x: Usuario(x[0],x[1],x[2])(registro) for registro in registros)
                #o asi
                #for registro in registros:
                #    usuario = Usuario(registro[0], registro[1], registro[2])
                #    usuarios.append(usuario)
                #o....
                return usuarios
            except Exception as e:
                print(e)
                sys.exit()
        
    
    @classmethod
    def insertar(cls, usuario_a_insertar):
        with CursorDelPool() as cursor:
            try:
                usuario_a_insertar = [usuario_a_insertar.username, usuario_a_insertar.password]
                cursor.execute(cls._INSERTAR, usuario_a_insertar)

                print("Usuario insertado con éxito")
                return cursor.rowcount
            except Exception as e:
                print(e)
                sys.exit()

    
    @classmethod
    def actualizar(cls, username_usuario_a_actualizar, password_usuario_a_actualizar, id_usuario_a_actualizar):
        with CursorDelPool() as cursor:
            try:
                usuario_a_actualizar = [username_usuario_a_actualizar, password_usuario_a_actualizar, id_usuario_a_actualizar]
                cursor.execute(cls._ACTUALIZAR, usuario_a_actualizar)
                
                print("Usuario actualizado con éxito")
                return cursor.rowcount
            except Exception as e:
                print(e)
                sys.exit()


    @classmethod
    def eliminar(cls,id_usuario_a_eliminar):
        with CursorDelPool() as cursor:
            try:
                cursor.execute(cls._ELIMINAR, id_usuario_a_eliminar)
                print("Usuario eliminado correctamente")
                return cursor.rowcount
            except Exception as e:
                print(e)
                sys.exit()


        
        
            
y = UsuarioDao()
yy = y.seleccionar()
print(yy)