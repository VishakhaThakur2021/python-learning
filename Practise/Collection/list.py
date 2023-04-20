# list -used to stor multiple item in single variable
# we can update and change any element in the list

food = ["hotdog", "noodles", "maggi"]
print(food)
food[0] = "sushi"

food.pop()  # remove last element
food.insert(0, "ice")
food.remove("noodles")
food.sort()
# food.clear()

for x in food:
    print(x)
