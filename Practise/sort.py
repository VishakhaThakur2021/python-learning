# sort() method -used with  lists but it doesn't work with tuples or other iterables that why we use sort function
# sort() function -used with iterables

student = ["apple", "mango", "banana", "kiwi"]
season = ["winter", "spring", "summer", "rainy"]

student.sort()
season.sort(reverse=True)  # we can reverse the sort list
for i in student:
    print(i)
for i in season:
    print(i)

tree = ("oak", "pine", "mango", "neem")  # this tuple will not work with above sort method , so we use sorted function

sorted_tree = sorted(tree)
for i in sorted_tree:
    print(i)
# how to work with 2d list

student_data = [("magnus", "P", 30), ("Aisa", "K", 78), ("Gini", "A", 65)]
student_tup = (("siwi", "W", 90), ("mili", "O", 56), ("eily", "R", 60))
# student_data.sort() # we can sort by first column with student name

# for i in student_data:
# print(i)
# grade=lambda grades:grades[1]
# student_data.sort(key=grade) # here we r using key to sort second column ,creating grade object and using lambda to sort with index 1
# for i in student_data:
# print(i)

age = lambda ages: ages[2]
# student_data.sort(key=age)  # here we r using key to sort third column ,creating age object and using lambda to sort with index 2
# for i in student_data:
#     print(i)

sort_student = sorted(student_tup, key=age)  # we can use sorted funtion too instead of sort method to deal with tuples
for i in sort_student:
    print(i)
