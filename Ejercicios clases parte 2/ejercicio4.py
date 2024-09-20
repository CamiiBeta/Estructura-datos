#Clase Círculo: Crea una clase Círculo con un atributo radio.
#Incluye métodos para calcular el área y la circunferencia del círculo.
import math
class Circulo:
    def __init__(self,radio:float):
        self.radio=radio

    def calcularArea(self):
        self.area=math.pi*self.radio**2
        print (f"el area del circulo es {self.area}")

    def calcularCircunferencia(self):
        self.circunferencia=2*math.pi*self.radio
        print (f"la circunferencia del circulo es {self.circunferencia}")

circulo1=Circulo(5)
circulo1.calcularArea()
circulo1.calcularCircunferencia()

        