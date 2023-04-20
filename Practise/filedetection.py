import os

path = "C:\\Users\\abhay\\Desktop\\documents.txt"

if os.path.exists(path):
    print("that location exists")
    if os.path.isfile(path):
        print("this is a file")
    elif os.path.isdir(path):
        print("this is a directory")
else:
    print("this location doesn't exist")

# read a file

try:
    with open('test.tx') as file:  # if user misspelled the file name as tx we need exception handling
        print(file.read())
except FileNotFoundError:
    print("file not found")

# write a file
text = "helo"
with open('test.txt', 'w') as file:
    file.write(text)
