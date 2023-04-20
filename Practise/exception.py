# exception =events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide:"))
    denominator = int(input("Enter a number to divide:"))

    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("you cant divide by zero ")
except ValueError as e:
    print(e)
    print("Enter only number plz ")
except Exception as e:
    print(e)
    print("Any error  ")
else:
    print(result)
finally:
    print("this block will always execute")
