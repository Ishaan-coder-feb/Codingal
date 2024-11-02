class student:
    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no
    def printDetails(self):
        print("Name-",self.name)
        print("Age-",self.age)
        print("roll_no-",self.roll_no)
Ishaan=student("Ishaan",11,5)
Ishaan.printDetails()
Anush=student("Anush",10,6)
Anush.printDetails()
