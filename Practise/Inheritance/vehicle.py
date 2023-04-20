# abstract classes -prevent a user from creating an object of that class
# * compels a user to override abstract methods in child classes

# abstart class- a class which contains one or more abstract method
#abstract method - a method which has declaration but doesn't have any implementation

from abc import ABC ,abstractmethod  #import abstract method

class Vehicle(ABC):

    @abstractmethod
    def drive(self):
     pass

class Car(Vehicle):
    def drive(self):
        print("this car is driving")

class Motorcycle(Vehicle):
    def drive(self):
        print("this car is driving")

vehicle=Vehicle()
car=Car()
motorcycle=Motorcycle()