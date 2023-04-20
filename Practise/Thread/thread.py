# thread - a flow of execution.like a seprate order of instructions.
#            however each thread takes a turn running to achieve concurrency
#            GIL=(global interpreter lock)
#                allow only one thread to hold the control of the python interpreter at any one time

# cpu bound - program/task spends most of its time waiting for internal events(cpu intensive)
#             use multi processing
#io bound-program/task spends most of its time waiting for external events(user input,web scraping)
#             use multi threading

import threading
import time



def drink_coffee():
    time.sleep(1)
    print("drink coffee")

def drink_juice():
    time.sleep(2)
    print("drink juice")

def drink_water():
    time.sleep(3)
    print("drink water")

#drink_coffee()
#drink_water()
#drink_juice()

x= threading.Thread(target=drink_coffee, args=())
x.start()

y= threading.Thread(target=drink_water,args=())
y.start()

z= threading.Thread(target=drink_juice,args=())
z.start()

x.join() # join helps to join all the threads in to one 
y.join()
z.join()

print(threading.activeCount())
print(threading.enumerate())  #we have one main thread responsible for running main thread and we can have another thread
                              #responsible for running other set of instructions
print(time.perf_counter())