import random

x = random.randint(1, 6)
print(x)

myList = ["rock", "paper", "scissor"]
z = random.choice(myList)
print(z)

cards = [1, 2, 3, 4, 5, "J", "k", "q"]
random.shuffle(cards)
print(cards)
