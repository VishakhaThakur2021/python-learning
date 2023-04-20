# if __name__ == '__main__'

# 1. Module can be run as  standalone program
# 2. Module can be imported and run by other modules
# python interpreter sets "special variable" one of which is "__name__"
# then python will excute code found with in __main__

import ifNameModuleTwo


def hello():
    print("hello")  # we can't print hello as standalone program


# print(__name__)                  # here variable name is assigned to __main__
# print(ifNameModuleTwo.__name__)  # here variable name is assigned to module name

if __name__ == '__main__':
    # print("running module directly")
    hello()
# else:
#    print("running module indirectly")
