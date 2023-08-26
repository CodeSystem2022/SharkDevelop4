from laboratorio_usuarios import usuario
from laboratorio_usuarios import usuario_DAO
from logger_base import log
opcion = None
while opcion != 5:
    print('Opcion: ')
    print('1. Listar Usuarios')
    print('2. Agregar Usuario')
    print('3. Actualizar Usuario')
    print('4. Eliminar Usuario')
    print('5. Salir')
    opcion = int(input('Digite la opcion (1-5): '))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Digite el nombre de usuario: ')
        password_var = input('Digite su contraseña: ')
        usuario = usuario(username=username_var, password=password_var)
        usuario_insertado = usuario_DAO.insertar(usuario)
        log.info(f'Usuario insertado: {usuario_insertado}')
    elif opcion == 3:
        id_usuario_var = int(input('Digite el id del usuario a modificar'))
        username_var = input("Digite el nombre del usuario a modificar: ")
        password_var = input("Digite la contraseña del usuario a modificar")
        usuario = usuario(id_usuario=id_usuario_var, username=username_var, password=password_var)
        usuario_actualizado = usuario_DAO.actualizar(usuario)
        log.info(f'Usuario actualizado: {usuario_actualizado}')
    elif opcion == 4:
        id_usuario_var = int(input("Digite el id del usuario a eliminar"))
        usuario = usuario(id_usuario=id_usuario_var)
        usuario_eliminado = usuario_DAO.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuario_eliminado}')
else:
    log.info('Salimos de la aplicacion, Hasta pronto!!')