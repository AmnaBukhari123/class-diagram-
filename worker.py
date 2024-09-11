from person import Person

class Worker(Person):
    def __init__(self, name, phone_number, cnic, address, worker_id):
        super().__init__(name, phone_number, cnic, address)
        self.worker_id = worker_id
        self.task = None 

    def assign_task(self, task):
        self.task = task

    def get_assigned_task(self):
        if self.task:
            return f"Worker {self.worker_id} is assigned to: {self.task}"
        else:
            return f"Worker {self.worker_id} has no assigned tasks."

    def __str__(self) -> str:
        return f"{super().__str__()}, Worker ID: {self.worker_id}"


