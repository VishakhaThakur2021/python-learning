# lambda = function written in one line using lambda keyword
#          accept any number of argument but only has one expression
#         (useful if needed for a short period of time,throw-away)

def multiply(x):
    return x * 2


print(multiply(2))

# above 3 line of code represented in one line by lambda

sum = lambda x: x * 2
# sum is function name = lambda x is parameter passed inside function : x*2 is return statement
substract = lambda x, y: x - y
add = lambda x, y, z: x + y + z
age_check = lambda age: True if age >= 3 else False

print(sum(3))
print(substract(4, 5))
print(add(3, 4, 5))
print(age_check(33))
