#method chaining - calling multiple method sequencially
#                   each call performs an action on the same object and returns self

class Human:
    def eat(self):
        print("human can eat")
        return self   # for method chaining we need to return something
    def sleep(self):
        print("human can sleep")
        return self
    def run(self):
        print("human can run")
        return self
    def work(self):
        print("human can work")
        return self

human = Human()
human.eat().work().run().sleep()
