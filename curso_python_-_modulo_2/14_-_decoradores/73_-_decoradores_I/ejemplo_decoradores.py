def funcion_decoradora(funcion):
    def funcion_interior():
        print("Antes de ejecutar la función")
        funcion()
        print("Después de ejecutar la función")
    return funcion_interior

@funcion_decoradora
def suma():
    print(2 + 2)
    
@funcion_decoradora    
def resta():
    print(4 - 2)
    
suma()
resta()