class Persona():
    def __init__(self, nombre, edad, domicilio):
        self.nombre = nombre
        self.edad = edad
        self.domicilio = domicilio

    def descripcion(self):
        print("Nombre:", self.nombre, "Edad:", self.edad, "Residencia:", self.domicilio)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_emp, edad_emp, domicilio_emp):
        super().__init__(nombre_emp, edad_emp, domicilio_emp)
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self):
        super().descripcion()
        
        print(f"Salario: {self.salario} \nAntigüedad: {self.antiguedad}")


antonio = Persona("Antonio", 55, "España")
antonio.descripcion()

manuel = Empleado(1500, 15, "Manuel", 55, "Colombia")
manuel.descripcion()

print(isinstance(manuel, Empleado))
print(isinstance(manuel, Persona))
print(isinstance(antonio, Persona))
print(isinstance(antonio, Empleado))



