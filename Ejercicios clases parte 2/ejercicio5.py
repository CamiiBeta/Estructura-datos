#Crea una clase Libro con atributos como título, autor, género y añoDePublicación. 
#Incluye métodos para obtener y establecer los valores de estos atributos, así como un método mostrarDetalles() que imprima la información del libro.

class Libro:
    def __init__(self, titulo:str,autor:str,genero:str,anoPublicacion:int):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        self.anoPublicacion=anoPublicacion

    def get_titulo(self)->str:
        return self.titulo
    
    def get_autor(self)->str:
        return self.autor
    
    def get_genero(self)->str:
        return self.genero
    
    def get_anoPublicacion(self)->int:
        return self.anoPublicacion
    
    def set_titulo(self, titulo:str)->str:
        self.titulo=titulo
    
    def set_autor(self, autor:str)->str:
        self.autor=autor

    def set_genero(self, genero:str)->str:
        self.genero=genero

    def set_anoPublicacion(self, anoPublicacion:int)->int:
        self.anoPublicacion=anoPublicacion

    def mostrarDetalles(self):
        print(f"El libro llamado {self.titulo},fue escrito por {self.autor}, es de género {self.genero}, y fue publicado en el año {self.anoPublicacion}")
    
libro1=Libro("El niño que perdió la guerra","Julia Navarro","Ficción",2024)
libro1.mostrarDetalles()
print(libro1.get_anoPublicacion())
libro1.set_anoPublicacion(2023)
libro1.mostrarDetalles()