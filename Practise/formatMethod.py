# str.format() =optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The" + animal + "jumped over the" + item)
print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))  # positional argument
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))  # keyword argument

number = 3.1459
num = 1000
print("The number pi is {:.3f}".format(number))
print("The number  is {:,}".format(num))
print("The number  is {:b}".format(num))
print("The number  is {:0}".format(num))
print("The number  is {:x}".format(num))
print("The number  is {:E}".format(num))
