from Car_Wash import Car_Wash

class Tier_3(Car_Wash):
    def __init__(self, car_wash_type, worker):
        super().__init__(car_wash_type)
        self.worker = worker

    def Wash_Car(self):
        return f"Soap + polish + inner clean car wash performed by {self.worker.Name}"

