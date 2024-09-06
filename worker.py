from person import Person

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


