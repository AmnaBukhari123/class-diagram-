class Vehicle:
    def __init__(self, vehicle_no_plate, car_model):
        self.vehicle_no_plate = vehicle_no_plate
        self.car_model = car_model


    def __str__(self) -> str:
        return f"Vehicle No Plate: {self.vehicle_no_plate}, Car Model: {self.car_model}"


