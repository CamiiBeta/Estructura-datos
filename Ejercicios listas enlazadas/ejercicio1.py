#Diseñe e implemente un sistema para el control de un sistema de un parque Zoologico 
#Crear una clase animal con los métodos y atributos básicos. 
# en uno de los atributos, debes indicar la edad y el tipo de animal (Águila, pantera, vaca, ...)

class Animal:
    def __init__(self, nombre:str, tipo:str, edad:int):
        self.nombre=nombre
        self.tipo=tipo
        self.edad=edad
    
    def __str__(self)->str:
        return f"Animal: {self.nombre}, Tipo: {self.tipo}, Edad: {self.edad} años"

class Nodo:
    def __init__(self,animal:Animal):
        self.animal=animal
        self.siguiente=None

class listaEnlazada:
    def __init__(self):
        self.cabeza=None
    
    def agregarAnimal(self, animal: Animal):
        if self.cabeza is None:
            self.cabeza = Nodo(animal)
            print(f"El animal {animal.nombre} se agrego al zoológico")
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                if actual.animal.nombre == animal.nombre:
                    print(f"El animal {animal.nombre} ya está en la lista.")
                    return
                actual = actual.siguiente
            else:
                actual.siguiente = Nodo(animal)
                print(f"El animal {animal.nombre} se agregó al zoológico")

    def listaBucle(self):
        if self.cabeza is None:
            print("La lista de animales está vacía.")
            return
        actual = self.cabeza
        while actual is not None:
            print(actual.animal)
            actual = actual.siguiente

    def imprimirListaRecursion(self):
        if self.cabeza is None:
            print("La lista de animales está vacía.")
        else:
            self.listaRecursion(self.cabeza)

    def listaRecursion(self, nodo:Animal):
        if nodo is None:
            return
        print(nodo.animal)
        self.listaRecursion(nodo.siguiente)


        




aguila = Animal("Águila", "Ave", 5)
pantera = Animal("Pantera", "Felino", 7)
vaca = Animal("Vaca", "Mamífero", 3)
zoologico = listaEnlazada()
zoologico.agregarAnimal(aguila)
zoologico.agregarAnimal(pantera)
zoologico.agregarAnimal(vaca)
zoologico.agregarAnimal(aguila)
zoologico.listaBucle()     
zoologico.imprimirListaRecursion()






    