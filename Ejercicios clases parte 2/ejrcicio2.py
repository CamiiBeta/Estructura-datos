#Clase CuentaBancaria: Crea una clase CuentaBancaria con atributos como titular (un objeto de la clase Persona), aldo y númeroDeCuenta. 
# Incluye métodos para depositar, retirar y consultarSaldo. 
# Asegúrate de manejar casos como retiros que exceden el saldo disponible.

class Persona:
    def __init__(self, nombre: str, edad: int, genero: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

class cuentaBancaria:
    def __init__(self,titular:Persona, nroCuenta:int,saldo:float):
        self.titular = titular
        self.nroCuenta= nroCuenta
        self.saldo=saldo

    def depositar(self):
        self.deposito=float(input("Ingrese cuanto saldo desea agregar a la cuenta:"))
        if self.deposito>0:
            self.saldo+=self.deposito
            print(f"El deposito fue realizo, tu nuevo saldo es de {self.saldo}")
        else:
            print("No se puede agregar cantidades negativas")
    
    def retirar(self):
        self.retiro=float(input("Ingrese cuanto saldo desea retirar de la cuenta:"))
        if self.retiro<self.saldo:
            if self.retiro>0:
                self.saldo-=self.retiro
                print(f"El retiro ha sido realizado con exito, tu nuevo saldo es {self.saldo}")
            else: 
                print(f"No se pueden retirar cantidades negativas o iguales a 0, intente nuevamente")
        elif self.retiro>self.saldo:
            print(f"Saldo insuficiente, no se pudo realizar el retiro, tu saldo actual es de: {self.saldo}")
        else:
            print("Cantidad no valida, intente nuevamente")    

    def consultarSaldo(self):
        (print(f"El saldo actual de la cuenta {self.nroCuenta} es: {self.saldo}"))
    
persona1=Persona("Ana",38,"femenino")
cuenta1=cuentaBancaria(persona1,"3000948",125000)
cuenta1.consultarSaldo()
cuenta1.depositar()
cuenta1.retirar()
    