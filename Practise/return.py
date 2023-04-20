# return statement - function send python  value/object back to the caller
# these function's value/object are known as function return value

def multiply(number1, number2):
    return number1 * number2


x = multiply(5, 6)
print(x)


# Keyword argument -argument preceded by identifier when we pass them to function,
# the order of argument doesn't matter,unlike positional
# python knows the name of the argument that function receives

def hello(first, last, name):
    print("hello " + first + " " + last + " " + " " + name)


hello(name="man", first="tan", last="hen")
