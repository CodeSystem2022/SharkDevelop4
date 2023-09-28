class Usuario:
    _contador_id = 0

    def __init__(self,  username=None, password=None):
        Usuario._contador_id+=1

        self._id_usuario = Usuario._contador_id
        self._username = username
        self._password = password
        

    @property
    def id_usuario(self):
        return self._id_usuario
    

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario


    @property
    def username(self):
        return self._username
        

    @username.setter
    def username(self, username):
        self._username = username


    @property
    def password(self):
        return self._password
    

    @password.setter
    def password(self, password):
        self._password = password


    def __str__(self) -> str:
        return f"{self._id_usuario} - {self._username} - {self.password}"




if __name__ == "__main__":
    
    miUser = Usuario(3,"miuser", "contraseña")
    miUser.__str__()
    print(miUser)
    print(miUser.id_usuario)