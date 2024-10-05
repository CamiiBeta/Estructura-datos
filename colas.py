import heapq

# Clase básica de Tarea con solo ID, prioridad y tiempo de ejecución
class Tarea:
    def __init__(self, id, prioridad, tiempo_ejecucion):
        self.id = id
        self.prioridad = prioridad
        self.tiempo_ejecucion = tiempo_ejecucion

    # Definimos el operador '<' para que la cola de prioridad funcione correctamente
    def __lt__(self, other):
        return self.prioridad < other.prioridad  # Menor número, mayor prioridad

# Función para crear tareas de ejemplo
def crear_tareas():
    return [
        Tarea("A", 2, 4),
        Tarea("B", 1, 2),
        Tarea("C", 3, 1),
        Tarea("D", 2, 3),
    ]

# Planificación por SJF (se ejecutan las tareas con menor tiempo de ejecución)
def planificacion_sjf(tareas):
    tareas.sort(key=lambda x: x.tiempo_ejecucion)  # Ordenar por tiempo de ejecución

    print("\n--- SJF ---")
    for tarea in tareas:
        print(f"Tarea {tarea.id}: Ejecutando con duración {tarea.tiempo_ejecucion}")

# Planificación por Prioridad (se ejecutan las tareas de mayor prioridad primero)
def planificacion_prioridad(tareas):
    cola_prioridad = []
    for tarea in tareas:
        heapq.heappush(cola_prioridad, tarea)  # Agregar tarea a la cola de prioridad

    print("\n--- Planificación por Prioridad ---")
    while cola_prioridad:
        tarea = heapq.heappop(cola_prioridad)
        print(f"Tarea {tarea.id}: Ejecutando con prioridad {tarea.prioridad}")

# Crear tareas y ejecutar ambos algoritmos
tareas = crear_tareas()
planificacion_sjf(tareas)

tareas = crear_tareas()
planificacion_prioridad(tareas)
