class Vehicle:
    def __init__(self, Vehicle_no_plate, car_model):
        self.Vehicle_no_plate = Vehicle_no_plate
        self.car_model = car_model


    def __str__(self) -> str:
        return f"Vehicle No Plate: {self.Vehicle_no_plate}, Car Model: {self.car_model}"


