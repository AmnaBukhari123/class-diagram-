from car_wash import CarWash
from worker import Worker

class Tier3(CarWash):
    def __init__(self,name, phone_number, cnic, address, worker_id, car_wash_type):
        super().__init__(car_wash_type)
        self.worker = Worker(name, phone_number, cnic, address, worker_id)

    def wash_car(self):
        return f"Soap + polish + inner clean car wash performed by {self.worker.name}"

