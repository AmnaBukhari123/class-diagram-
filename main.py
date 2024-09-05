class Person:
    def __init__(self, Name, Phone_Number, CNIC, Address):
        self.Name = Name
        self.Phone_Number = Phone_Number
        self.CNIC = CNIC
        self.Address = Address
        

    def __str__(self) -> str:
        return f"Name: {self.Name}, Phone: {self.Phone_Number}, CNIC: {self.CNIC}, Address: {self.Address}"
    

class Vehicle:
    def __init__(self, Vehicle_no_plate, car_model):
        self.Vehicle_no_plate = Vehicle_no_plate
        self.car_model = car_model


    def __str__(self) -> str:
        return f"Vehicle No Plate: {self.Vehicle_no_plate}, Car Model: {self.car_model}"



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



class Worker(Person):
    def __init__(self, Name, Phone_Number, CNIC, Address, Worker_Id):
        super().__init__(Name, Phone_Number, CNIC, Address)
        self.Worker_Id = Worker_Id
        self.task = None 

    def assign_task(self, task):
        self.task = task

    def get_assigned_task(self):
        if self.task:
            return f"Worker {self.Worker_Id} is assigned to: {self.task}"
        else:
            return f"Worker {self.Worker_Id} has no assigned tasks."

    def __str__(self) -> str:
        return f"{super().__str__()}, Worker ID: {self.Worker_Id}"



class Register_entries:
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
    
    
class Car_Wash:
    def __init__(self, car_wash_type):
        self.car_wash_type = car_wash_type

    def Wash_Car(self):
        return "Washing car"


class Tier_1(Car_Wash):
    def Wash_Car(self):
        return f"Soap only car wash performed!"


class Tier_2(Car_Wash):
    def Wash_Car(self):
        return f"Soap and polish car wash performed!"


class Tier_3(Car_Wash):
    def __init__(self, car_wash_type, worker):
        super().__init__(car_wash_type)
        self.worker = worker

    def Wash_Car(self):
        return f"Soap + polish + inner clean car wash performed by {self.worker.Name}"


class CarWash_Record:
    def __init__(self, worker, vehicle):
        self.worker = worker
        self.vehicle = vehicle

    def __str__(self):
        return f"Car Wash Record - Vehicle No : {self.vehicle.Vehicle_no_plate} washed by worker {self.worker.Worker_Id}"


def main():
   
    workers = [
        Worker(Name="Sara Jones", Phone_Number="123-456-7890", CNIC="12345-6789012-3", Address="123 Main St", Worker_Id="W001"),
        Worker(Name="John Smith", Phone_Number="234-567-8901", CNIC="23456-7890123-4", Address="234 Oak St", Worker_Id="W002"),
        Worker(Name="Emily Davis", Phone_Number="345-678-9012", CNIC="34567-8901234-5", Address="345 Pine St", Worker_Id="W003"),
        Worker(Name="Michael Brown", Phone_Number="456-789-0123", CNIC="45678-9012345-6", Address="456 Maple St", Worker_Id="W004"),
        Worker(Name="Linda Johnson", Phone_Number="567-890-1234", CNIC="56789-0123456-7", Address="567 Elm St", Worker_Id="W005")
    ]

    
    customers = [
        Customer(Name="Tom Williams", Phone_Number="987-654-3210", CNIC="98765-4321098-7", Address="456 Third St", Customer_Id="C001", subscription_Id="S001", Vehicle_no_plate="ABC-123"),
        Customer(Name="Anna Lee", Phone_Number="876-543-2109", CNIC="87654-3210987-6", Address="567 Fourth St", Customer_Id="C002", subscription_Id="S002", Vehicle_no_plate="DEF-456"),
        Customer(Name="James Wilson", Phone_Number="765-432-1098", CNIC="76543-2109876-5", Address="678 Fifth St", Customer_Id="C003", subscription_Id="S003", Vehicle_no_plate="GHI-789"),
        Customer(Name="Sophia Martinez", Phone_Number="654-321-0987", CNIC="65432-1098765-4", Address="789 Sixth St", Customer_Id="C004", subscription_Id="S004", Vehicle_no_plate="JKL-012"),
        Customer(Name="Daniel Brown", Phone_Number="543-210-9876", CNIC="54321-0987654-3", Address="890 Seventh St", Customer_Id="C005", subscription_Id="S005", Vehicle_no_plate="MNO-345")
    ]

    
    for customer in customers:
        customer.Vehicle.car_model = "Car Model for " + customer.Customer_Id

    
    register_entries = [Register_entries(car_entry_time="10:00 AM", car_leaving_time="11:00 AM", customer=cust) for cust in customers]

   
    car_wash_records = [CarWash_Record(worker=workers[i % len(workers)], vehicle=customers[i % len(customers)].Vehicle) for i in range(len(customers))]

    
    tier1_wash = Tier_1(car_wash_type="Tier 1")
    tier2_wash = Tier_2(car_wash_type="Tier 2")
    tier3_washes = [Tier_3(car_wash_type="Tier 3", worker=workers[i % len(workers)]) for i in range(len(customers))]

    
    for worker in workers:
        worker.assign_task(f"Washing car for customer {worker.Worker_Id}")

    print("--------Automatic Car Wash System---------")
    print("1. Workers Details")
    print("2. Customers Details")
    print("3. Vehicles Details")
    print("4. Register Entries")
    print("5. Perform Tier 1 Car Wash")
    print("6. Perform Tier 2 Car Wash")
    print("7. Perform Tier 3 Car Wash")
    print("8. Car Wash Record")
    print("9. Check Worker Task")
    print("10. Check Customer Subscription")
    print("11. Update Customer Subscription")
    print("12. Exit")
    
    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            for worker in workers:
                print(worker)
        elif choice == '2':
            for customer in customers:
                print(customer)
        elif choice == '3':
            for customer in customers:
                print(customer.Vehicle)
        elif choice == '4':
            for entry in register_entries:
                print(entry)
        elif choice == '5':
            print(tier1_wash.Wash_Car())
        elif choice == '6':
            print(tier2_wash.Wash_Car())
        elif choice == '7':
            for wash in tier3_washes:
                print(wash.Wash_Car())
        elif choice == '8':
            for record in car_wash_records:
                print(record)
        elif choice == '9':
            for worker in workers:
                print(worker.get_assigned_task())
        elif choice == '10':
            for customer in customers:
                print(customer.get_subscription_status())
        elif choice == '11':
            customer_id = input("Enter customer ID to update subscription: ")
            new_subscription_Id = input("Enter new subscription ID: ")
            for customer in customers:
                if customer.Customer_Id == customer_id:
                    customer.update_subscription(new_subscription_Id)
                    print(f"Subscription for customer {customer_id} updated to {new_subscription_Id}")
                    break
            else:
                print("Customer ID not found.")
        elif choice == '12':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
