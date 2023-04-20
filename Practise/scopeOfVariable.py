# scope- the reason where a variable is recognized
# A variable is only available from inside the region where it is created
# A globally and local version of variable can be created

name = "vishu"  # global variable,available inside and outside of a function


def display_name():
    name = "last"
    print(name)  # local variable,available inside a function


print(name)
