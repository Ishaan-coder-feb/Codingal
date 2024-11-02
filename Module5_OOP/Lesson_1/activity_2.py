class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Create an object of the Vehicle class and pass the maximum speed and mileage
car = Vehicle(150, 12000)

# Print the values of max_speed and mileage using the object
print("Max Speed:", car.max_speed)
print("Mileage:", car.mileage)