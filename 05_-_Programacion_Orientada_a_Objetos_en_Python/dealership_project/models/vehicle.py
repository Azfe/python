import locale

# Establecer la configuración regional a España
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')  # En Windows puede que necesites 'Spanish_Spain.1252'. Sustituir por 'es_ES.UTF-8'

class Vehicle:
    def __init__(self, license_plate, car_brand, car_model, year, mileage, price, id_owner=None, is_new=True):
        self.license_plate = license_plate
        self.car_brand = car_brand
        self.car_model = car_model
        self.year = year
        self.mileage = mileage
        self.price = price
        self.id_owner = id_owner
        self.is_new = is_new
        self.available = True
        
        if self.is_new and self.id_owner is not None:
            raise ValueError("Un coche nuevo no debe tener propietario asignado.")
        
    def check_availability(self):
        return self.available
    
    def get_price(self):
        return self.price
        
    def __str__(self):
        estado = "Fábrica" if self.is_new else "Usado"
        propietario = f"Cliente {self.id_owner}" if self.id_owner else "Concesionario"
        # price_format = f"{self.get_price():,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        price_format = locale.currency(self.price, symbol=False, grouping=True)
        return f"{self.car_brand} {self.car_model} ({self.year}) - {self.license_plate} - {price_format}€ - {estado} - {propietario}" 