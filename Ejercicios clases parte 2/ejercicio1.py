#Clase Persona: Crea una clase Persona con atributos como nombre, edad y género. Incluye métodos para obtener y establecer los valores de estos atributos, así como un método presentarse() que imprima una breve descripción de la persona.

class Persona:
    def __init__(self, nombre: str, edad: int, genero: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def get_nombre(self) -> str:
        return self.nombre

    def get_edad(self) -> int:
        return self.edad

    def get_genero(self) -> str:
        return self.genero

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def set_edad(self, edad: int):
        self.edad = edad

    def set_genero(self, genero: str):
        self.genero = genero

    def presentacion(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años y soy de genero {self.genero}")
persona1 = Persona("Carlos", 28, "masculino")
persona1.presentacion()
print(persona1.get_nombre())
persona1.get_edad()
persona1.get_genero()
persona1.set_nombre("Camilo")
persona1.get_nombre()
persona1.presentacion()