class Vehicle:
    def __init__(self, name, max_speed, capacity):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity

    def display_info(self):
        return f"Vehicle Name: {self.name}, Max Speed: {self.max_speed} km/h, Capacity: {self.capacity} passengers"


class Bus(Vehicle):
    def __init__(self, name, max_speed, capacity, fare_per_person):
        super().__init__(name, max_speed, capacity)
        self.fare_per_person = fare_per_person

    def calculate_total_fee(self, passengers):
        if passengers > self.capacity:
            return "Error: Number of passengers exceeds capacity."
        total_fee = passengers * self.fare_per_person
        return f"Total fee for {passengers} passengers: ₹{total_fee}"


# Example usage
bus = Bus("City Bus", 80, 50, 20)  # Name, Max Speed, Capacity, Fare per Person

print(bus.display_info())
print(bus.calculate_total_fee(30))  # Calculate fee for 30 passengers
print(bus.calculate_total_fee(60))  # Exampl
