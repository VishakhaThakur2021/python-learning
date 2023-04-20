# higher function order - 1. accepts a function as an argument
#                        2. returns a function

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):  # this is higher order function which is calling lower order function
    text = func("hello")
    print(text)


hello(quiet)  # we can pass any lower function as an argument to higher function
hello(loud)


#  2. returns a function

def divisor(x):  # this is higher function
    def dividend(y):
        return (y / x)

    return dividend  # this function is lower function which is returned


divide = divisor(2)
print(divide(10))  # we can pass lower function argument from here
