#super - functions() used to give access to the parents class
#       Returns a temporary object of a parent class when used

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
class Square(Rectangle):
    def __init__(self, width, height):
        super().__init__(width,height)
    def area(self):
        return self.height*self.width

class Cube(Rectangle):
    def __init__(self, width, height,length):
        super().__init__(width,height)
        self.length=length
    def volume(self):
        return self.height*self.width*self.length

square=Square(3,3)
cube=Cube(3,3,3)

print(square.area())
print(cube.volume())


