from customer import Customer
from worker import Worker
from register_entries import RegisterEntries
from tier1 import Tier1
from tier2 import Tier2
from tier3 import Tier3
from car_wash_record import CarWashRecord

def main():
    workers = [
        Worker(name="Sara Jones", phone_number="123-456-7890", cnic="12345-6789012-3", address="123 Main St", worker_id="W001"),
        Worker(name="John Smith", phone_number="234-567-8901", cnic="23456-7890123-4", address="234 Oak St", worker_id="W002"),
        Worker(name="Emily Davis", phone_number="345-678-9012", cnic="34567-8901234-5", address="345 Pine St", worker_id="W003"),
        Worker(name="Michael Brown", phone_number="456-789-0123", cnic="45678-9012345-6", address="456 Maple St", worker_id="W004"),
        Worker(name="Linda Johnson", phone_number="567-890-1234", cnic="56789-0123456-7", address="567 Elm St", worker_id="W005")
    ]

    customers = [
        Customer(name="Tom Williams", phone_number="987-654-3210", cnic="98765-4321098-7", address="456 Third St", customer_id="C001", subscription_id="S001", vehicle_no_plate="ABC-123", car_model="Model A"),
        Customer(name="Anna Lee", phone_number="876-543-2109", cnic="87654-3210987-6", address="567 Fourth St", customer_id="C002", subscription_id="S002", vehicle_no_plate="DEF-456", car_model="Model B"),
        Customer(name="James Wilson", phone_number="765-432-1098", cnic="76543-2109876-5", address="678 Fifth St", customer_id="C003", subscription_id="S003", vehicle_no_plate="GHI-789", car_model="Model C"),
        Customer(name="Sophia Martinez", phone_number="654-321-0987", cnic="65432-1098765-4", address="789 Sixth St", customer_id="C004", subscription_id="S004", vehicle_no_plate="JKL-012", car_model="Model D"),
        Customer(name="Daniel Brown", phone_number="543-210-9876", cnic="54321-0987654-3", address="890 Seventh St", customer_id="C005", subscription_id="S005", vehicle_no_plate="MNO-345", car_model="Model E")
    ]

    register_entries = [
        RegisterEntries(car_entry_time="10:00 AM", car_leaving_time="11:00 AM", 
                        name=cust.name, phone_number=cust.phone_number, 
                        cnic=cust.cnic, address=cust.address, 
                        customer_id=cust.customer_id, subscription_id=cust.subscription_id, 
                        vehicle_no_plate=cust.vehicle.vehicle_no_plate, car_model=cust.vehicle.car_model)
        for cust in customers
    ]

    
    car_wash_records = [
        CarWashRecord(
            name=workers[i % len(workers)].name,
            phone_number=workers[i % len(workers)].phone_number,
            cnic=workers[i % len(workers)].cnic,
            address=workers[i % len(workers)].address,
            worker_id=workers[i % len(workers)].worker_id,
            vehicle_no_plate=customers[i % len(customers)].vehicle.vehicle_no_plate,
            car_model=customers[i % len(customers)].vehicle.car_model
        )
        for i in range(len(customers))
    ]

    
    tier1_wash = Tier1(car_wash_type="Tier 1")
    tier2_wash = Tier2(car_wash_type="Tier 2")
    tier3_washes = [Tier3(name=workers[i % len(workers)].name, 
                          phone_number=workers[i % len(workers)].phone_number, 
                          cnic=workers[i % len(workers)].cnic, 
                          address=workers[i % len(workers)].address, 
                          worker_id=workers[i % len(workers)].worker_id, 
                          car_wash_type="Tier 3") for i in range(len(customers))]

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
                print(customer.vehicle)
        elif choice == '4':
            for entry in register_entries:
                print(entry)
        elif choice == '5':
            print(tier1_wash.wash_car())
        elif choice == '6':
            print(tier2_wash.wash_car())
        elif choice == '7':
            for wash in tier3_washes:
                print(wash.wash_car())
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
            new_subscription_id = input("Enter new subscription ID: ")
            for customer in customers:
                if customer.customer_id == customer_id:
                    customer.update_subscription(new_subscription_id)
                    print(f"Subscription for customer {customer_id} updated to {new_subscription_id}")
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
