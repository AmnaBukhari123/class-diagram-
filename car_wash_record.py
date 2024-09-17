from worker import Worker
from vehicle import Vehicle

class CarWashRecord:
    def __init__(self, name, phone_number, cnic, address, worker_id, vehicle_no_plate, car_model):
        self.worker = Worker(name, phone_number, cnic, address, worker_id)
        self.vehicle = Vehicle(vehicle_no_plate, car_model)

    def __str__(self):
        return f"Car Wash Record - Vehicle No : {self.vehicle.vehicle_no_plate} washed by worker {self.worker.worker_id}"

