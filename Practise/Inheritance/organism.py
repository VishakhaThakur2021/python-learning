#multi level inheritance - when a derived child (class) inherit another derived child (class)
#                         its like a grant tree ,grandparent -->parent-->child
class Organism:

    alive =True

    def walk(self):
        print("this animal is walking")

class Animal(Organism):
    def eat(self):
        print("this animal is eating")

class Fish(Animal):
    def swim(self):
        print("this animal is swimming")

fish = Fish()
print(fish.alive)
fish.eat()
fish.swim()

