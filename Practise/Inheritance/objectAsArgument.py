# object as argument - we can pass any object as an argument to a function


class Vehicle:

    color =None

def change_colour(vehicle,color): # make sure this function is not part of class and first argument name can be anything
 #                                   vehicle is an object
    vehicle.color =color

car_1=Vehicle()
car_2=Vehicle()
car_3=Vehicle()



change_colour(car_1,"red")
change_colour(car_2,"yellow")
change_colour(car_3,"green")

print(car_1.color)
print(car_2.color)
print(car_3.color)

