#ejercicio 4

class Usuario:
    def __init__(self, nombreUsuario: str, contraseña: str):
        self.nombreUsuario = nombreUsuario
        self.contraseña = contraseña

    def login(self, contraseñaIngresada: str):
        if contraseñaIngresada == self.contraseña:
            print(f"El usuario {self.nombreUsuario} ha iniciado sesio correctamente")
        else:
            print("Contraseña incorrecta")

class Administrador(Usuario):
    def gestion(self):
        print(f"El administrador {self.nombreUsuario} está gestionando los usuarios")

class Cliente(Usuario):
    def compras(self):
        print(f"El cliente {self.nombreUsuario} está realizando una compra")

admin = Administrador("admin123", "adminpass")
cliente = Cliente("cliente001", "password")

admin.login("adminpass")
admin.gestion()

cliente.login("password")
cliente.compras()
