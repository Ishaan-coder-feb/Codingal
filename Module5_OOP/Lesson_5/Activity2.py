from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        """Abstract method that must be implemented by all subclasses"""
class Human(Animal):
    def move(self):
        """Implementation of move for a human"""
        print("Humans can move or run")
class Dog(Animal):
    def move(self):
        """Implementation of move for a Dog"""
        print("Dogs can run and jump.")
class Fish(Animal):
    def move(self):
        """Implementation of move for a Fish"""
        print("Fish can swim.")
def main():
    human = Human()
    dog = Dog()
    fish = Fish()
    print("Demonstrating animal movements:")
    human.move()
    dog.move()
    fish.move()
if __name__ == "__main__":
    main()

