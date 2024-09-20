#PARTE 1
#Crear una clase llamada Vehículo, esta clase debe recibir 2 parámetros, marca y combustible; 
# la clase también debe contener dos métodos encender y arrancar. 
# Instanciar la clase y usar el método mágico __str__ para imprimir la marca y el combustible usado

class Vehiculo:
    def __init__ (self,marca:str,combustible:str, tipo:str):
        self.marca=marca
        self.combustible=combustible
        self.tipo=tipo
        self.encendido=False

    def encender(self):
        self.capacidadCombustible=float(input(f"Cuál es la capacidad total del/de la {self.tipo} en combustible(galones)?:"))
        self.nivelCombustible=float(input(f"Cuál es el nivel actual del/de la {self.tipo} de combustible(galones)?:"))
        if self.nivelCombustible > 0:
            print(f"El/ la {self.tipo} se ha encendido con exito")
            self.encendido=True 
            if self.nivelCombustible/self.capacidadCombustible<=0.1:
                print(f"ADVIRTENCIA: el/la {self.tipo} tiene combustible por debajo del 10%, necesita tanquearse")
        else:
            print(f"No se puede encender el/la {self.tipo} porque no tiene suficiente combustuble")

    def arrancar(self):
        if not self.encendido:
            print (f"El/la {self.tipo} no está encendido, primero enciendalo")
            return
        self.galonesMilla = float(input(f"Cuánto galones consume el/la {self.tipo} por milla?:"))
        self.millas = float(input(f"Cuántas millas quieres recorrer con el/la {self.tipo}?:"))
        self.consumoTotal= self.galonesMilla * self.millas
        if self.nivelCombustible-self.consumoTotal<=0:
            self.nivelCombustible=0
            print(f"El/la {self.tipo} se quedo sin combustible y se detuvo")
            self.encendido=False
        else:
            self.nivelCombustible-=self.consumoTotal
            print(f"El/la {self.tipo} reccorrio {self.millas} millas y le quedan {self.nivelCombustible} galones")
    

    def __str__(self)->str:
        return f"El vehiculo es un/una {self.tipo} de marca {self.marca} y usa combustible {self.combustible}"

# Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo. 
#Realizar dos instancias de las nuevas clases creadas e imprimir el objeto instanciado

class Moto(Vehiculo):
    def __init__(self, marca: str, combustible: str):
        super().__init__(marca, combustible, "moto")

class Carro(Vehiculo):
    def __init__(self, marca: str, combustible: str):
        super().__init__(marca, combustible, "carro")

moto1=Moto("yamaha","gasolina")
carro1=Carro("renault","corriente")
print(moto1)
print(carro1)
moto1.encender()
carro1.encender()
moto1.arrancar()
carro1.arrancar()

#La clase Vehiculo, debe tener una propiedad llamada tipo (esta contendrá el tipo de vehiculo - Carro o Moto -)
#Esta propiedad debe ser seteada al momento de instanciar la clase Carro o Moto 
#al momento de imprimir el objeto debe indicar el tipo de vehiculo junto con el texto mostrado anteriormente 

#Hacer control de encendido de los vehiculos, para esto al momento de usar el método encender
#se debe validar el nivel de combustible del vehiculo (medida dada en galones) no este por debajo de un 10%
#si este tiene un nivel muy bajo, mostrar la advertencia que necesita ir a la gasolinera. 

#Debes hacer un ejercicio donde por medio de un método, el vehículo de marcha y haga un consumo de combustible a medida que este funcione, 
#cuando llegue a los niveles de combustible definidos en el punto anterior, muestre la advertencia y si esta llega a cero, detenga la marcha 

