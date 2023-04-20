# map() - applies a function to each item in an iterable(list,tuple etc)
# map(function,iterable)

store = [("shirt", 20.00),
         ("pant", 56.00)]

to_euro = lambda data: (data[0], data[1] * 0.82)  # to_euro is function name ,data is parameter (check lambda.py file)

store_euro = list(map(to_euro, store))  # map(function,iterable),storing new map to the list
print("---------- to euro")
for i in store_euro:
    print(i)

print("--------- to dollar")

# if we want to convert to dollar
to_dollar = lambda data: (data[0], data[1] / 0.82)
store_dollar = list(map(to_dollar, store))  # map(function,iterable)
for i in store_dollar:
    print(i)
