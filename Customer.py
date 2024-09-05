from Person import Person 
from Vehicle import Vehicle

class Customer(Person):
    def __init__(self, Name, Phone_Number, CNIC, Address, Customer_Id, subscription_Id, Vehicle_no_plate):
        super().__init__(Name, Phone_Number, CNIC, Address)
        self.Customer_Id = Customer_Id
        self.subscription_Id = subscription_Id
        self.Vehicle_no_plate = Vehicle_no_plate
        self.Vehicle = Vehicle(Vehicle_no_plate, car_model=None)


    def update_subscription(self, new_subscription_Id):
       self.subscription_Id = new_subscription_Id


    def get_subscription_status(self):
        return f"Customer {self.Customer_Id} has subscription ID: {self.subscription_Id}"

    def __str__(self) -> str:
        return f"{super().__str__()}, Customer ID: {self.Customer_Id}, Subscription ID: {self.subscription_Id}, Vehicle No Plate: {self.Vehicle_no_plate}"


