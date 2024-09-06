class RegisterEentries:
    def __init__(self, car_entry_time, car_leaving_time, customer):
        self.car_entry_time = car_entry_time
        self.car_leaving_time = car_leaving_time
        self.customer = customer

    def __str__(self):
        return (
            f"Customer ID: {self.customer.Customer_Id}, "
            f"Vehicle No Plate: {self.customer.Vehicle.Vehicle_no_plate}, "
            f"Entry Time: {self.car_entry_time}, "
            f"Leaving Time: {self.car_leaving_time}"
        )
    
 