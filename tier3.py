from car_wash import CarWash

class Tier3(CarWash):
    def __init__(self, car_wash_type, worker):
        super().__init__(car_wash_type)
        self.worker = worker

    def wash_car(self):
        return f"Soap + polish + inner clean car wash performed by {self.worker.name}"

