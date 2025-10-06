class Square:
    def __init__(self, side):
        self.side = side
    def area(self):  
        print(self.side * self.side)
class Triangle:
    def __init__(self, base):
        self.base = base
    def area(self):  
        print(self.base * (self.base/2))
objMul=Square(5)
objDiv=Triangle(6)

for shape in (objMul,objDiv):
    shape.area()

    
    