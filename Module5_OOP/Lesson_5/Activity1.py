from abc import ABC, abstractmethod

class AbstaractClass(ABC):
    def print(self,value):
        print("The passed value is",value)

    @abstractmethod     
    def task(self):
        print("This is an abstract method")
class Test_class(AbstaractClass):
    def task(self):
        print("We have successfully implemented abstraction")
obj=Test_class()
obj.task()
obj.print(28)


