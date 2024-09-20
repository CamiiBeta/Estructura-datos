#Crea una clase Canción con atributos como título, artista, álbum y duración. 
# Incluye métodos para obtener y establecer los valores de estos atributos, así como un método reproducir() que simule la reproducción de la canción (puedes simplemente imprimir un mensaje).

class Cancion:
    def __init__(self, titulo:str, artista:str, album:str, duracion:float):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

    def get_titulo(self) -> str:
        return self.titulo

    def get_artista(self) -> str:
        return self.artista

    def get_album(self) -> str:
        return self.album

    def get_duracion(self) -> float:
        return self.duracion
    
    def set_titulo(self, titulo: str):
        self.titulo = titulo

    def set_artista(self, artista: str):
        self.artista = artista

    def set_album(self, album: str):
        self.album = album

    def set_duracion(self, duracion: float):
        self.duracion = duracion

    def reproducir(self):
        print (f"Se está reproduciendo {self.titulo} de {self.artista}, DURACIÓN: {self.duracion}")
    
cancion1=Cancion("Save Your Tears","The weeknd", "Blinding Lights", 3.47)
cancion1.reproducir()

    
