name = "bro code"

print(name.count("o"))
print(name.capitalize())
print(len(name))
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.replace("o", "i"))

# slicing - creating a substring by extracting from another string
# indexing[]  ,  [start:stop:step]
name = "Bro Code"
index = name[0:3]  # or name[:3]
print(index)
index2 = name[4:]  # or  name[4:8]
print(index2)
index3 = name[::2]  # [0:end:2]
print(index3)
# reversing string
index4 = name[::-1]  # [0:end:-1]
print(index4)

# slice()
web = "https://google.com"
var1 = slice(8, -4)
print(web[var1])
