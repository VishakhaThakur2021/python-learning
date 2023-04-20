# walrus operator :=
# assigns value to variable as part of a larger expression


foods = list()
while True:
    food = input("what food u like ? ")
    if food == "quit":
        break
    foods.append(food)
# or

foods = list()
while True:
    food = input("what food u like ? ") != "quit"  # by using := we can reduce line of code
    foods.append(food)
