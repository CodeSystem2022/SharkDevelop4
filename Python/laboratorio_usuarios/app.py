from usuario import Usuario
from usuario_DAO import UsuarioDao
opcion = None

while opcion != 5:
    print("""
        1. Seleccionar
        2. Insertar
        3. Actualizar
        4. Eliminar
        5. Salir
          """)
    opcion = int(input("Digite una opcion: "))
    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        print(usuarios)

    elif opcion==2:
        user = input("Diga un nombre de usuario: ")
        password = input("Diga una contraseña")
        nuevo_usuario = Usuario(user, password)
        UsuarioDao.insertar(nuevo_usuario)

    elif opcion==3:
        id = int(input("diga el numero de id del usuario a modificar"))
        user = input("Diga un nombre de usuario: ")
        password = input("Diga una contraseña")
        UsuarioDao.actualizar(user,password,id)
    elif opcion==4:
        opcion = int(input("Está seguro que desea eliminar un usuario (Yes=1/No=0): "))
        if opcion==1:
            UsuarioDao.eliminar(int(input("Diga el número de id del usuario que desea eliminar")))

    else: 
        print("Muchas gracias por elegirnos!")


    
