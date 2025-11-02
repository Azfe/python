class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        
    def __repr__(self):
        return f"Empleado({self.nombre} que trabaja como {self.cargo}, tiene un salario de {self.salario} €)"
    
lista_empleados = [
    Empleado("Juan", "Director", 75000),
    Empleado("Ana", "Presidente", 65000),
    Empleado("Antonio", "Administrativo", 25000),
    Empleado("Maria", "Administrativo", 27000),
    Empleado("Marta", "Director", 80000),
]

salarios_altos = list(filter(lambda empleado: empleado.salario > 50000, lista_empleados))

for empleado_salario in salarios_altos:
    print(empleado_salario)

