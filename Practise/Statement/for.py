# For -statement that will execute its block of code for limited amount of time
# while--->unlimited
# For--->Limited
import time

for i in range(10):
    print(i + 1)

for i in range(50, 100, 2):
    print(i + 1)

for i in "Magic":
    print(i)

for second in range(10, 0, -1):
    print(second)
    time.sleep(1)
print("Happy new year")  # make sure this print is not indended and outside for loop
