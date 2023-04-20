class Car:
    wheel = 4  # class variable are declared outside the constructor

    def __init__(self, make, model, color):
        self.make = make  # instance variable are declared inside constructor
        self.model = model  # instance variable
        self.color = color  # instance variable

    def Drive(self):
        print("driving")

    def Stop(self):
        print("stopped")
