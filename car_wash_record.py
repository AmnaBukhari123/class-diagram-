class CarWashRecord:
    def __init__(self, worker, vehicle):
        self.worker = worker
        self.vehicle = vehicle

    def __str__(self):
        return f"Car Wash Record - Vehicle No : {self.vehicle.Vehicle_no_plate} washed by worker {self.worker.Worker_Id}"

