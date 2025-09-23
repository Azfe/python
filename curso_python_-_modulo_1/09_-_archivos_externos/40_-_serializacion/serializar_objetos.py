import pickle

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enMarcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True
        
    def estado(self):
        return(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enMarcha} \nAcelerando: "
              f"{self.acelera} \nFrenando: {self.frena}")
        

# instancias
coche1 = Vehiculo("Mazda", "MX5")
coche2 = Vehiculo("Seat", "León")
coche3 = Vehiculo("Opel", "Astra")

coches = [coche1, coche2, coche3]

# Manejo de fichero
fichero = open("losCoches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero)
