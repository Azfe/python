class Coche():
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos
        
        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()
            if(chequeo):
                return "El coche está en marcha"
            else:
                return "Se detectaron problemas en el chequeo"                
        else:
            return "El coche está apagado"        
    
    def estado(self):
        return f"El coche tiene {self.__ruedas} ruedas. Un largo de {self.__largoChasis} cm. y un ancho de {self.__anchoChasis} cm."
    
    def __chequeo_interno(self):
        print("Realizando chequeo interno...")
        
        self.combustible = "fail"
        self.aceite = "ok"
        self.puertas_cerradas = "cerradas"
        
        if(self.combustible == "ok" and self.aceite == "ok" and self.puertas_cerradas == "cerradas"):
            return True
        else:
            return False
            
            
        
# Ejemplo de uso    
# instancia de clase
miCoche = Coche()
miCoche2 = Coche()

print(miCoche.arrancar(True))
print(miCoche.estado())

print(miCoche2.arrancar(False))
print(miCoche2.estado())