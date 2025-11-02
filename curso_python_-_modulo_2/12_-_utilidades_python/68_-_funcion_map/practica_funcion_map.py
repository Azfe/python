class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        
    def __repr__(self):
        return f"Empleado({self.nombre} que trabaja como {self.cargo}, tiene un salario de {self.salario} €)"
    
lista_empleados = [
    Empleado("Juan", "Director", 7500),
    Empleado("Ana", "Presidente", 6500),
    Empleado("Antonio", "Administrativo", 2500),
    Empleado("Maria", "Administrativo", 2700),
    Empleado("Marta", "Director", 8000),
]

def calculo_comision(empleado):
    if(empleado.salario < 3000):
        empleado.salario = empleado.salario * 1.03
    return empleado

lista_empleados_comision = list(map(calculo_comision, lista_empleados))

for empleado in lista_empleados_comision:
    print(empleado)