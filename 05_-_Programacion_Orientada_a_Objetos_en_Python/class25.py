class Persona:
    def __init__(self, dni, nombre, apellidos, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.is_alive = True
        
class Cliente(Persona):
    def __init__(self, dni, nombre, apellidos, edad, id_cliente):
        super().__init_(dni, nombre, apellidos, edad) # Llama al constructor de Persona
        self.id_cliente = id.cliente
        
class Empleado(Persona):
    def __init__(self,)