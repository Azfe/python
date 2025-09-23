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
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enMarcha} \nAcelerando: "
              f"{self.acelera} \nFrenando: {self.frena}")

class Furgoneta(Vehiculo):
    
    def cargar(self, carga):
        self.cargado=carga
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta está vacía"
    
    
class Moto(Vehiculo):
    # def __init__(self, marca, modelo):
    #     super(marca, modelo)
    caballito = "A dos ruedas"
    
    def hacer_caballito(self):
        self.caballito = "haciendo el caballito"
        
    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enMarcha} \nAcelerando: "
              f"{self.acelera} \nFrenando: {self.frena} \n{self.caballito}")
        
        
class V_Electrico():
    def __init__(self):
        self.autonomia = 100
    
    def cargar_energia(self):
        self.cargando = True
        
class Bicicleta_electrica(V_Electrico, Vehiculo): # Herencia múltiple
    def __init__(self):
        pass
