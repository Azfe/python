from datetime import date

class Purchase:
    def __init__(self, id_customer, vehicle, purchase_date=None, final_price=None):
        self.id_customer = id_customer
        self.vehicle = vehicle
        self.purchase_date = purchase_date or date.today()
        self.final_price = final_price or vehicle.price
    
    def __str__(self):
        return f"Compra: {self.vehicle.license_plate} por cliente {self.id_customer} el {self.purchase_date}"