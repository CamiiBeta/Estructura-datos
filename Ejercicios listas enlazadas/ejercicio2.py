#Diseña e implementa un sistema de gestión de tareas utilizando listas enlazadas. 
#Cada tarea tendrá las siguientes propiedades:

from datetime import datetime

class Tarea:
    def __init__(self, descripcion:str, prioridad:int, fechaVencimiento:str):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fechaVencimiento = datetime.strptime(fechaVencimiento, "%d/%m/%Y")

    def __str__(self):
        return (f"Descripción: {self.descripcion}, "
                f"Prioridad: {self.prioridad}, "
                f"Fecha de Vencimiento: {self.fechaVencimiento.strftime('%d/%m/%Y')}")
    
class Nodo:
    def __init__(self, tarea:Tarea):
        self.tarea = tarea
        self.siguiente = None 

class listaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregarTarea(self, tarea: Tarea):
        nuevoNodo = Nodo(tarea)
        if self.cabeza is None or (tarea.prioridad < self.cabeza.tarea.prioridad or (tarea.prioridad == self.cabeza.tarea.prioridad and tarea.fechaVencimiento < self.cabeza.tarea.fechaVencimiento)):
            nuevoNodo.siguiente = self.cabeza
            self.cabeza = nuevoNodo
            print(f"La tarea {tarea.descripcion} fue agregada con exito")
        else:
            actual = self.cabeza
            while actual.siguiente is not None and (actual.siguiente.tarea.prioridad < tarea.prioridad or(actual.siguiente.tarea.prioridad == tarea.prioridad and actual.siguiente.tarea.fechaVencimiento < tarea.fechaVencimiento)):
                actual = actual.siguiente
            nuevoNodo.siguiente = actual.siguiente
            actual.siguiente = nuevoNodo
            print(f"La tarea {tarea.descripcion} fue agregada con exito")   

    def eliminarTarea(self, descripcion: str):
        actual = self.cabeza
        anterior = None
        if actual is None:
            print("La lista esta vacía, no hay tareas para eliminar")
            return
        while actual is not None:
            if actual.tarea.descripcion == descripcion:
                if anterior is None: 
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                print(f"La tarea {descripcion} fue eliminada correctamente")
                return
            anterior = actual
            actual = actual.siguiente
        print(f"No se encontro la tarea {descripcion}")

    def mostrarTareas(self):
        if self.cabeza is None:
            print("No hay tareas en la lista")
        else:
            actual = self.cabeza
            while actual is not None: 
                print(actual.tarea)
                actual = actual.siguiente
        

    def buscarTarea(self, descripcion: str):
        actual = self.cabeza
        while actual is not None:
            if actual.tarea.descripcion == descripcion:
                print(f"Tarea encontrada: {actual.tarea}")
                return actual.tarea
            actual = actual.siguiente
        print(f"Tarea {descripcion} no encontrada")
        return None
    
    def marcarCompletada(self, descripcion: str):
        self.eliminarTarea(descripcion)

listaTareas = listaEnlazada()
tarea1 = Tarea("Comprar comida", 2,"25/09/2024")
tarea2 = Tarea("Terminar proyecto", 1, "20/09/2024")
tarea3 = Tarea("Hacer ejercicio", 3, "22/09/2024")
listaTareas.agregarTarea(tarea1)
listaTareas.agregarTarea(tarea2)
listaTareas.agregarTarea(tarea3)
listaTareas.mostrarTareas()
listaTareas.eliminarTarea("Comprar comida")
listaTareas.eliminarTarea("Ir al cine")
listaTareas.mostrarTareas()
listaTareas.buscarTarea("Leer un libro")
listaTareas.buscarTarea("Terminar proyecto")
listaTareas.marcarCompletada("Hacer ejercicio")
listaTareas.mostrarTareas()
