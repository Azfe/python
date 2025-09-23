class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")
        
class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")
        
class Camion()        :
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

# Polimorfismo 
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
    
miVehiculo = Coche()
desplazamientoVehiculo(miVehiculo)
    
miVehiculo = Moto()
desplazamientoVehiculo(miVehiculo)

miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)
    