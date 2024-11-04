class Dog:
    animal = "Dog"
    
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def display_details(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")
        print() 
dog1 = Dog("Labrador", "Golden")
dog2 = Dog("Bulldog", "White")
dog1.display_details()
dog2.display_details()
