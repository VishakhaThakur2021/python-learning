class Animal:

    alive =True

    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("this animal is sleeping")

class Hawk(Animal):
    print("this animal is hawking")
class Rabbit(Animal):
    print("this animal is jumping")
class Fish(Animal):
    print("this animal is swimming")

rabbit =Rabbit()
hawk =Hawk()
fish =Fish()

print(rabbit.alive)
hawk.eat()
fish.sleep()



