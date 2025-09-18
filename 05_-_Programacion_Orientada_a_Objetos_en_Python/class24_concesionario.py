# Concesionario de coches: Compra y venta de vehículos.
# Los usuarios pueden preguntar los vehículos disponibles, su precio y comprarlos.

from datetime import date
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
    
class Customer:
    def __init__(self, id_customer, name, lastname, email, age, dni, registration_date):
        self.id_customer = id_customer
        self.name = name
        self.lastname = lastname
        self.email = email
        self.age = age
        self.dni = dni
        self.registration_date = registration_date  
        self.vehicles_owned = []
        
    def get_owned_vehicles(self, vehicle_list):
        # self.vehicles_owned = [v for v in vehicle_list if v.id_owner == self.id_customer]
        for v in vehicle_list: # Comprobar si vehículo es del cliente
            if v.id_owner == self.id_customer:
                self.vehicles_owned.append(v)
                # print(f"El vehículo es de {self.name}")
        # return self.vehicles_owned    
        print(f"\n🚗 Vehículos en propiedad de {self.name}:")
        for vo in self.vehicles_owned:
            print(f" - {vo}")
            
    def inquire_car(self, vehicle):
        if vehicle.check_availability():
            print(f"El vehículo '{vehicle.car_brand} {vehicle.car_model}' está disponible y cuesta {vehicle.get_price():,.2f}€.")
        else:
            print(f"El vehículo '{vehicle.car_brand} {vehicle.car_model}' no se encuentra disponible.")
            
        # availability = "disponible" if vehicle.check_availability() else "no disponible"
        # print(f"El coche {vehicle.car_brand} {vehicle.car_model} está {availability} y cuesta {vehicle.get_price()}.")

    def __str__(self):
        return f"{self.id_customer} - {self.name} {self.lastname} - {self.dni} - {self.email} - {self.age} años - {self.registration_date}"
    
class Purchase:
    def __init__(self, id_customer, vehicle, purchase_date=None, final_price=None):
        self.id_customer = id_customer
        self.vehicle = vehicle
        self.purchase_date = purchase_date or date.today()
        self.final_price = final_price or vehicle.price
    
    def __str__(self):
        return f"Compra: {self.vehicle.license_plate} por cliente {self.id_customer} el {self.purchase_date}"
    
class Sale:
    _id_sales_counter = 1
    
    def __init__(self, id_customer, vehicle, sale_date=None, sale_price=None):
        self.id_sale = Sale._id_sales_counter
        Sale._id_sales_counter += 1
        
        self.id_customer = id_customer
        self.vehicle = vehicle
        self.sale_date = sale_date or date.today()
        self.sale_price = sale_price or vehicle.price  
        
    def __str__(self):
        return f"Venta #{self.id_sale}: {self.vehicle.license_plate} por cliente {self.id_customer} el {self.sale_date}"

class Dealership:
    _id_customers_counter = 1    
    
    def __init__(self, id_dealership):
        self.id_dealership = id_dealership
        self.vehicles = []
        self.customers = []
        self.sales = []
        self.purchases = []
        
    def register_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"\n El siguiente vehículo ha sido añadido al concesionario: \n"
            f"Marca: '{vehicle.car_brand}'\n"
            f"Modelo: '{vehicle.car_model}'\n"
            f"Matrícula: '{vehicle.license_plate}'"            
        )        
    
    def register_customer(self, customer):
        self.customers.append(customer)        
        customers_counter = len(self.customers) # Actualiza el contador de ID para cada nuevo cliente
        customer.id_customer = customers_counter        
        print(f"El cliente '{customer.name} {customer.lastname}' ha sido dado de alta con ID: {customer.id_customer}.")
        
    def show_available_vehicles(self):        
        print("Vehículos disponibles:")
        for vehicle in self.vehicles:
            estado = "Fábrica" if vehicle.is_new else "Usado"
            if vehicle.available:
                print(f"- {vehicle.car_brand} {vehicle.car_model} - ({vehicle.year}) - {vehicle.mileage}Km - {vehicle.price}€ - Estado: {estado}")
    
    def sell_vehicle(self, license_plate, buyer_id):
        for vehicle in self.vehicles:
            if vehicle.license_plate == license_plate and vehicle.available:
                vehicle.available = False
                vehicle.id_owner = buyer_id
                purchase = Purchase(buyer_id, vehicle)
                self.sales.append(purchase)                
                print(f"Vehículo vendido a cliente {buyer_id}: {vehicle}")
                return
            
        print("Vehículo no disponible o no encontrado.")                
    
    def buy_vehicle_from_customer(self, vehicle, seller_id):
        vehicle.id_owner = None # El concesionario lo adquiere
        vehicle.avaible = True
        self.vehicles.append(vehicle)
        sale = Sale(seller_id, vehicle)
        self.purchases.append(sale)
        
        print(f"Vehículo comprado al cliente {seller_id}: {vehicle}")
        
    def list_sales(self):
        print("\nVentas realizadas:")
        for sale in self.sales:
            print(f"Venta: #{sale}")
            
    def list_purchases(self):
        print(f"\nCompras realizadas:")
        for p in self.purchases:
            print(f"Compra: #{p}")
            
    def list_customers(self):
        print("\nLista de clientes:")
        for c in self.customers:
            print(f"Cliente: {c}")
    

# Ejemplo de uso
# Crear concesionario
dealer = Dealership(1)

# Registro de clientes
cliente1 = Customer(1, "Alex", "Zapata", "alex@email.com",41, "48497586A", date.today())
dealer.register_customer(cliente1)
cliente2 = Customer(1, "Laura", "García", "laura@email.com", 30, "12345678X", date.today())
dealer.register_customer(cliente2)
cliente3 = Customer(1, "Gael", "Martínez", "gael@email.com", 22, "72168348Z", date.today())
dealer.register_customer(cliente3)

# Mostrar lista de clientes
dealer.list_customers()

# Cliente vende su coche al concesionario
vehiculo1 = Vehicle(
    license_plate="9138KTJ",
    car_brand="Skoda", 
    car_model="Fabia", 
    year=2019, 
    mileage=80000, 
    price=8000, 
    id_owner=cliente1.id_customer, 
    is_new=False)
dealer.buy_vehicle_from_customer(vehiculo1, cliente1.id_customer)

# Otro cliente compra el coche
dealer.sell_vehicle(vehiculo1.license_plate, cliente2.id_customer)

# Se registran nuevos coches
vehiculo2 = Vehicle("4578THD", "Kia", "Sportage", 2025, 0, 36000)
dealer.register_vehicle(vehiculo2)
vehiculo3 = Vehicle("4578THD", "Toyota", "Yaris", 2023, 0, 25000)
dealer.register_vehicle(vehiculo3)
vehiculo4 = Vehicle(
    license_plate="0000XYZ",
    car_brand="Tesla",
    car_model="Model Y",
    year=2025,
    mileage=0,
    price=48000
    # id_owner no se pasa → se asume que es del concesionario
)
dealer.register_vehicle(vehiculo4)

# Cliente compra nuevo coche
dealer.sell_vehicle(vehiculo2.license_plate, cliente3.id_customer)
dealer.sell_vehicle(vehiculo4.license_plate, cliente3.id_customer)

# Listar coches disponibles
dealer.show_available_vehicles()

# Lista las ventas realizadas
dealer.list_sales()

# Lista las compras realizadas
dealer.list_purchases()

# Consultar disponibilidad
cliente1.inquire_car(vehiculo2)
cliente1.inquire_car(vehiculo3)
cliente2.inquire_car(vehiculo1)
cliente3.inquire_car(vehiculo4)

# Supongamos que dealer.vehicles contiene todos los vehículos
mis_coches = cliente3.get_owned_vehicles(dealer.vehicles)
mis_coches = cliente2.get_owned_vehicles(dealer.vehicles)
