# break -used to terminate the loop entirely
# continue-skips to the next iteration of the loop
# pass-does nothing act as placeholder

while True:
    name = input("Enter ur name")
    if name != "":
        break  # it will come out of the loop once expectation meets to True

phone = "123-456-789"
for i in phone:
    if i == "-":
        continue  # it will skip -
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        pass  # it will pass 13 number
    else:
        print(i)
