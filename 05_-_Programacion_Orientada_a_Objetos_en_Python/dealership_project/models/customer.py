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