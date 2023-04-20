# functions to variable

def hello():
    print("assign")


hi = hello
hi()  # when we assign hi to hello both memory location are same, it will print same results
hello()

say = print  # even we can assign print to say variable and both will print
say("hello i am print now ")
print("hello i am print now ")
