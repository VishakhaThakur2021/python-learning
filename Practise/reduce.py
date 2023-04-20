# reduce() - apply a function to an iterable and reduce it to single cumulative value
#            perform function on first two element and repeats process until 1 value remains
# reduce(function,iterable)


import functools

letters = ["H", "E", "L", "L", "O"]

word = functools.reduce(lambda x, y: x + y,
                        letters)  # it takes lambda function(x , y are first two element) and iterable list(letters)
# ["HE","L","L","O"]
# ["HEL","L","O"]
# ["HELL","O"]
# ["HELLO"]
print(word)
