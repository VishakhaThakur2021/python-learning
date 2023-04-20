# tuple- collection which is ordered and unchangeable,used to group together related data
# represented by ()

student = ("name", 21, "male", "name")

print(student.count("name"))
print(student.index("name"))

for z in student:
    print(z)
if "name" in student:
    print("name is present")
