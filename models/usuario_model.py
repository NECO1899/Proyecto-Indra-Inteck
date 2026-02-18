class UsuarioModel:
    def autenticar(self, usuario, clave):
        return usuario == "admin" and clave == "1234"