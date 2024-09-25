#Ejercicio 1:
class Empleado:
    def __init__(self, nombre: str, salario: float, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

class Gerente(Empleado):
    def __init__(self, nombre: str, salario: float, departamento: str, equipo: list):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo

    def supervisarAEquipo(self):
        print(f"El /la gerente {self.nombre} supervisa a {len(self.equipo)} empleados.")

class Desarrollador(Empleado):
    def __init__(self, nombre: str, salario: float, departamento: str, lenguajeDeProgramación: str):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramación = lenguajeDeProgramación

    def escribirCodigo(self):
        print(f"El/la desarrollador/a {self.nombre} está escribiendo código en {self.lenguajeDeProgramación}.")

equipo = [Empleado("Carlos", 3000, "Desarrollo"), Empleado("Ana", 3200, "Desarrollo")]
gerente = Gerente("Laura", 5000, "Gerencia", equipo)
desarrollador = Desarrollador("Juan", 4000, "Desarrollo", "Python")

gerente.supervisarAEquipo()
desarrollador.escribirCodigo()
