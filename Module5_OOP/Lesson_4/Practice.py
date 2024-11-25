class Student:
    _schoolName="Vidya mandir school"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self) :
        print("This is private function")
        print("Here I can access school name :",self._schoolName)
obj=Student("Ishaan",11)
print(obj.display())          
