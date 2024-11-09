class fruit:
    def __init__(self,colour,taste):
        self.colour=colour
        self.taste=taste
    def details(self):
        print(f"Colour:{self.colour}")
        print(f"Taste:{self.taste}")
fruitobj=fruit("peach","sweet")
fruitobj.details()


