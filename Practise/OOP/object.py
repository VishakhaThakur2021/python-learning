from car import Car

car1 = Car("2003", "suzuki", "black")
Car.wheel = 5  # class variable can be called with class name and user reassign the value
car1.Drive()
print(car1.wheel)  # class variable can be called with object name
