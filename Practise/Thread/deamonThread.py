# deamon thread = a thread that runs in the background, not important for the program to run
#                your program will not wait for deamon threads to complete before exiting
#                non-deamon thread cannot normally be killed,stay alive until task is complete
# ex -garbage collection , background tasks


import threading
import time


def timer():  # this function will log the time after user has looged in
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for ", count, "seconds")


x = threading.Thread(
    target=timer)  # this thread will be running in background , even after typing ok for do u wish to exit
# x =threading.Thread(target=timer, daemon=True) # to kill the background thread we use daemon =true , to kill the background thread 
x.start()

answer = input("Do u wish to exit:")  # this instruction is running under main thread
