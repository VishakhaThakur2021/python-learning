# set - A set is unordered ,unindexed and No duplicates values are allowed

utensils = {"spoon", "plate", "knife", "bottle", "bottle"}
utensils2 = {"glass", "cup", "knife"}

utensils.add("cold drink")
print(utensils.difference(utensils2))
utensils.update(utensils2)  # it will update utensils with all the items in utensils2
dinner = utensils.union(utensils2)

for x in dinner:
    print(x)
