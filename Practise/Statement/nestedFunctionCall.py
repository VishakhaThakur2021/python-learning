# nested function call - function calls inside other function calls
#                       inner most functions are resolved first
#                       returned value is used as argument for the next outer function

# num =input("Enter a number")
# num =float(num)
# num=abs(num)

print(round(abs(float(input("Enter whole number")))))
