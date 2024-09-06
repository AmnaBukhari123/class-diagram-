class Person:
    def __init__(self, Name, Phone_Number, CNIC, Address):
        self.Name = Name
        self.Phone_Number = Phone_Number
        self.CNIC = CNIC
        self.Address = Address
        

    def __str__(self) -> str:
        return f"Name: {self.Name}, Phone: {self.Phone_Number}, CNIC: {self.CNIC}, Address: {self.Address}"
    
