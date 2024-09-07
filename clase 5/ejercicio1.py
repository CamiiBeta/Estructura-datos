#Crear una clase llamada vehiculo, esta clase debe recibir dos parametros: marca y combustible, la clase también debe contener dos metodos, encender y arrancar.
#Instanciar la clase y usar el metodo magico __str__ para imprimir l marca y el combustible usado

class Vehiculo:
    def __init__(self,marca:str,combustible:str):
        self.marca=marca
        self.combustible=combustible
    def encender(self ):
        pass
    def arrancar(self ):
        pass
    def __str__(self ):
        return f"El vehiculo de marca {self.marca} utiliza combustible {self.combustible}"
    
carro=Vehiculo("toyota","corriente")
print(carro)
print(type(carro))

#Crear dos clases, moto y carro, estas clases deben estar heredadas de la clase vehiculo
#Realizar dos instancias de las nuevas clases creaas e imprimir el objeto instanciado:

class Moto(Vehiculo):
    def __init__(self,marca:str,combustible:str):
        super().__init__(marca,combustible)
class Carro(Vehiculo):
    pass

motocicleta= Moto("Honda","corriente")
miCarro= Carro("Mazda","extra")
print(motocicleta)
print(miCarro)