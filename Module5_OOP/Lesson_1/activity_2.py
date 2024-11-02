class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
car = Vehicle(150, 12000)
print("Max Speed:", car.max_speed)
print("Mileage:", car.mileage)
