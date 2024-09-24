#Crea una clase Estudiante con atributos como nombre, edad, curso y calificaciones (una lista o arreglo). 
#Incluye métodos para agregar calificaciones, calcular el promedio y determinar si el estudiante aprobó o reprobó el curso.

class Estudiante:
    def __init__(self,nombre:str,edad:int,curso:str):
        self.nombre=nombre
        self.edad=edad
        self.curso=curso
        self.calificaciones=[]
        self.aprobado=False

    def __str__(self):
        return f"Nombre del estudiante:{self.nombre}, Edad:{self.edad}, Curso:{self.curso}, Promedio:{self.calcularPromedio()},Estado:{self.aprobar()}"
    
    def agregarCalificacion(self,calificacion:int):
        if 0 <= calificacion <= 5:
            self.calificaciones.append(calificacion)
        else:
            print ("Calificación no válida, las notas son de 0 a 5")
        
    def calcularPromedio(self):
        if len(self.calificaciones)==0:
            print("No hay calificaciones disponibles")
            return 0
        else:
            self.promedio=sum(self.calificaciones)/len(self.calificaciones)
            print ("El promedio de tus notas es", self.promedio )
            return self.promedio
        
    def aprobar(self):
        if self.promedio is not None:
            if self.promedio>=3:
                print (f"Has aprobado el curso, tu nota final es de {self.promedio}")
                self.aprobado=True
                return "Estudiante aprobado"
            else:
                print (f"No aprobaste el curso, tu nota final es de {self.promedio}")
                self.aprobado=False
                return "Estudiante no aprobado"
            
        
            
estudiante = Estudiante("Juan Pérez", 20, "Matemáticas")
estudiante.agregarCalificacion(4.5)
estudiante.agregarCalificacion(3.2)
estudiante.agregarCalificacion(2.8)
estudiante.calcularPromedio()
estudiante.aprobar()
print(estudiante)    


            

        