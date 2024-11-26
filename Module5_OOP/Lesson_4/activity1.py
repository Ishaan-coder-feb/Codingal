class MyClass:
    def __init__(self):
        self.__privateVar = 42
    def __privMeth(self):
        print("This is a private method.")
    def hello(self):
        print(f"The value of privateVar is: {self.__privateVar}")
        self.__privMeth()
my_object = MyClass()
my_object.hello()
