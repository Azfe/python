import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)
        
    def __str__(self):
        return f"{self.nombre} {self.genero} {self.edad}"
    
class ListaPersonas:
    personas = []
    
    def __init__(self):
        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)
        
        try:
            self.personas = pickle.load(listaDePersonas)
            print(f"Se cargaron {len(self.personas)} personas del fichero externo.")
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
    
    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
        
    def mostrarPersonas(self):
        print("\nMostrar personas:")
        for p in self.personas:
            print(p)
            
    def guardarPersonasEnFicheroExterno(self):
        ListaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, ListaDePersonas)
        ListaDePersonas.close()
        del(ListaDePersonas)
        
    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.persona:
            print(p)
                

miListaPersonas = ListaPersonas()

p = Persona("Ana", "Femenino", 34)
miListaPersonas.agregarPersonas(p)

p = Persona("Juan", "Masculino", 47)
miListaPersonas.agregarPersonas(p)

p = Persona("Pilar", "Femenino", 22)
miListaPersonas.agregarPersonas(p)

miListaPersonas.mostrarPersonas()