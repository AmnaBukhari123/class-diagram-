from Customer import Customer
from Worker import Worker
from Register_entries import Register_entries
from Tier_1 import Tier_1
from Tier_2 import Tier_2
from Tier_3 import Tier_3 
from CarWash_Record import CarWash_Record
  
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
