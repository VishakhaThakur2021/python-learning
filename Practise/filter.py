# filter()- creates a collection of elements from an iterable for which a function returns true
# filter(function,iterable)

student = [("deny", 33),
           ("maria", 16),
           ("mia", 23),
           ("lidia", 43)]

age = lambda data: data[1] >= 18  # here function returns true,for this criteria

age_list = list(filter(age, student))  # here we are creating seperate list for new collection

for i in age_list:
    print(i)
