# if statement - a block of code which will be executed when condition is true

age = int(input("what is your age "))

if age >= 18:
    print("you are eligible")
elif age < 18:
    print("you are not eligible")
else:
    print("not applicable")

# logical operator(and,or,not) use to check two or more conditions
temp = int(input("what is temperature outside"))

if temp >= 0 and temp <= 30:  # both are true
    print("temperature is good")
if temp <= 0 or temp >= 30:
    print("temperature not good")
# elif not(temp >= 0 and temp <= 30):
#    print("temp is moderate")
else:
    print("no value provided")
