#Clase Rectángulo: Crea una clase Rectángulo con atributos base y altura. 
#Incluye métodos para calcular el área y el perímetro del rectángulo.

class Rectangulo:
    def __init__(self, base:float, altura:float):
        self.base=base
        self.altura=altura
    
    def calcularArea(self):
        self.area=(self.altura*self.base)
        print (f"El area del rectangulo es {self.area}")
    
    def calcularPerimetro(self):
        self.perimetro=(2*self.altura)+(2*self.base)
        print (f"El perimetro del rectangulo es {self.perimetro}")
    
rectangulo1=Rectangulo(0.25,3)
rectangulo1.calcularArea()
rectangulo1.calcularPerimetro()