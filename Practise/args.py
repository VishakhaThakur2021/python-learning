# *args -parameter that add all the argument into a tuple
# it is useful so that a function accept a varying amount of argument

def add(*args):
    sum = 0
    args = list(args)  # that why we need to convert tuple to a list , inorder to assign new value to tuple
    args[0] = 0  # if try to assign new value to tuple , it wont be allowed

    for x in args:
        sum += x
    return sum


print(add(1, 2, 3, 4, 5, 6))  # arguments are inside tuple


# **kwargs -parameter that will pack all the items in to a dictionary
# it is useful so that function can accept a varying amount of keyword argument

def hello(**kwargs):
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="name", last="surname", middle="middle")
