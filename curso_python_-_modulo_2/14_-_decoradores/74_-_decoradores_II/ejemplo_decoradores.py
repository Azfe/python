def funcion_decoradora(funcion):
    def funcion_interior(*args, **kwargs):
        print("Antes de ejecutar la función")
        funcion(*args, **kwargs)
        print("Después de ejecutar la función")
    return funcion_interior

@funcion_decoradora
def suma(num1, num2, num3):
    print(num1 + num2 + num3)
    
@funcion_decoradora    
def resta(num1, num2):
    print(num1 - num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(2, 2, 2)
resta(2, 2)

potencia(base=5, exponente=3)
