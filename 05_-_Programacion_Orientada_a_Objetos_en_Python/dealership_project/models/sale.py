from datetime import date

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