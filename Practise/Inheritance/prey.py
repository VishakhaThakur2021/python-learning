#multiple inheritance - when a child class derived from more than one parent

class Prey:
    def flee(self):
        print("this animal flee")
class Predator:
    def hunt(self):
        print("this animal is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

hawk = Hawk()
rabbit=Rabbit()
fish=Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
