class Person:
    def __init__(self, name, phone_number, cnic, address):
        self.name = name
        self.phone_number = phone_number
        self.cnic = cnic
        self.address = address
        

    def __str__(self) -> str:
        return f"Name: {self.name}, Phone: {self.phone_number}, CNIC: {self.cnic}, Address: {self.address}"
    
