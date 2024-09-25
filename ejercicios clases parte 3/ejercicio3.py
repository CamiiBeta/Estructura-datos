#Ejercicio 3
class Electrodomestico:
    def __init__(self, marca: str, modelo: str, consumoEnergetico: str):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergetico = consumoEnergetico

    def encender(self):
        pass

class Lavadora(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumoEnergetico: str, capacidad: float):
        super().__init__(marca, modelo, consumoEnergetico)
        self.capacidad = capacidad

    def encender(self):
        print(f"La lavadora {self.marca} se encendió")
        self.iniciarCicloDeLavado()

    def iniciarCicloDeLavado(self):
        print(f"La lavadora {self.marca} con capacidad de {self.capacidad}kg está lavando")

class Refrigerador(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumoEnergetico: str, tieneCongelador: bool):
        super().__init__(marca, modelo, consumoEnergetico)
        self.tieneCongelador = tieneCongelador

    def encender(self):
        print(f"El refrigerador {self.marca} se encendió")
        self.regularTemperatura()

    def regularTemperatura(self):
        print(f"El refrigerador {self.marca} está regulando la temperatura. Congelador: {'Sí' if self.tieneCongelador else 'No'}")


lavadora = Lavadora("LG", "X100", "A++", 8)
refrigerador = Refrigerador("Samsung", "FrostFree", "A+", True)

lavadora.encender()
refrigerador.encender()
