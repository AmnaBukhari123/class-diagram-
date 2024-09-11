from person import Person 
from vehicle import Vehicle

class Customer(Person):
    def __init__(self, name, phone_number, cnic, address, customer_id, subscription_id, vehicle_no_plate):
        super().__init__(name, phone_number, cnic, address)
        self.customer_id = customer_id
        self.subscription_id = subscription_id
        self.vehicle_no_plate = vehicle_no_plate
        self.vehicle = Vehicle(vehicle_no_plate, car_model=None)


    def update_subscription(self, new_subscription_id):
       self.subscription_id = new_subscription_id


    def get_subscription_status(self):
        return f"Customer {self.customer_id} has subscription ID: {self.subscription_id}"

    def __str__(self) -> str:
        return f"{super().__str__()}, Customer ID: {self.customer_id}, Subscription ID: {self.subscription_id}, Vehicle No Plate: {self.vehicle_no_plate}"


