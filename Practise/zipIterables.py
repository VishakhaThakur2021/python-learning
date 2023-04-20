# zip (*iterables) = aggregate elements from two or more iterables (list,tuple,sets etc)
#                    creates a zip object with paired elements stored in tuples for each element

username = ["Dude", "Bro", "Mister"]
password = ("pass@word", "abc123", "guest")
date = ["1/3/2009", "2/5/2006", "2/6/2003"]

add = zip(username, password, date)  # aggregate elements from two or more iterables
for i in add:
    print(i)
user = zip(username, password)
user1 = zip(username, password)
# we can change zip type to any iterable (list,dictionary etc)
user = list(zip(username, password))
for i in user:
    print(i)

user1 = dict(zip(username, password))
for key, value in user1.items():
    print(key + ":" + value)
