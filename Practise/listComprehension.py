# list comprehension - a way to create a new list with less syntax
#                    list[expression for item in iterable]
#                   list[expression for item in iterable if condition]
#                   list[expression (if/else) for item in iterable]

square = []  # create an empty list
for i in range(1, 11):  # create a for loop
    square.append(i * i)  # define what each loop iteration should do
print(square)

# we can rewrite the above line of code in one line as
# list[expression for item in iterable]
square = [i * i for i in range(1, 11)]
print(square)

# let's try to write list comprehension for lambda function
student = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

# passed=list(filter(lambda x: x>=60,student)) #lambda
passed = [i for i in student if i >= 60]  # list[expression for item in iterable if condition ]

passed = [i if i >= 60 else Failed for i in student]  # list[expression (if/else) for item in iterable ]

print(passed)
