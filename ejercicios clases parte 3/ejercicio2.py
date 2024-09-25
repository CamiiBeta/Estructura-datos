class FiguraGeometrica:
    def calcularArea(self):
        pass

class Triangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        self.area=(self.base*self.altura)/2
        print (f"El área del triangulo es: {self.area}")
        return self.area

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float):
        self.lado = lado

    def calcularArea(self):
        self.area=self.lado ** 2
        print(f"El area del cuadrado es: {self.area}")
        return self.area

triangulo = Triangulo(5, 10)
cuadrado = Cuadrado(4)
triangulo.calcularArea()
cuadrado.calcularArea()
