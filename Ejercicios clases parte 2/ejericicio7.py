#Crea una clase Producto con atributos como nombre, precio y cantidadDisponible. 
# Incluye métodos para obtener y establecer los valores de estos atributos, 
#así como un método calcularTotal() que calcule el costo total de una cierta cantidad de productos.

class Producto:
    def __init__(self,nombre:str,precio:float, cantidadDisponible:int):
        self.nombre=nombre
        self.precio=precio
        self.cantidadDisponible=cantidadDisponible

    def __str__(self) -> str:
        return f"Nombre del producto: {self.nombre}, Precio:{self.precio}, Cantidad disponible:{self.cantidadDisponible}"

    def get_nombre(self)->str:
        return self.nombre
    
    def get_precio(self)->float:
        return self.precio

    def get_cantidadDisponible(self)->int:
        return self.cantidadDisponible
    
    def set_nombre(self,nombre:str):
        self.nombre=nombre

    def set_precio(self,precio:float):
        self.precio=precio

    def set_cantidadDisponible(self,cantidadDisponible:int):
        self.cantidadDisponible=cantidadDisponible

    def calcularTotal(self,cantidad:int):
        if cantidad>0:
            if cantidad <= self.cantidadDisponible:
                self.precioTotal=cantidad*self.precio
                print("El total de la compra fue",self.precioTotal)
                return self.precio
            else:
                print("No hay suficientes cantidades del producto")
                return    
        else:
            print("Cantidad no válida")

sabanas=Producto("Sabanas",5.00,2)
print(sabanas)
sabanas.calcularTotal(2)
sabanas.calcularTotal(3)
sabanas.calcularTotal(0)