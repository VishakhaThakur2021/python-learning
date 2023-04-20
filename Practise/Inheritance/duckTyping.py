#duck typing - concept where the class of an object is less important than the methods/attributes
#              class type is not checked if minimum methods/attributes are present
#              if it walk like a duck, if it talk like a duck then it must be a duck

class Duck:

    def walk(self):
        print("walk like a duck")
    def talk(self):
        print("talk like a duck")

class Chicken:
    def walk(self):
        print("walk like a duck")
    def talk(self):
        print("talk like a duck")

class Person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caught the clitter")

duck=Duck()
chicken=Chicken()
person=Person()

person.catch(duck)
person.catch(chicken)

