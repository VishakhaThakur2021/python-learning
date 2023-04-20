# inner loop -inner loop will finish all its iteration first before finishing one iteration for outer loop

rows = int(input("Enter rows:"))
columns = int(input("Enter columns:"))
symbol = input("Enter symbol")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
