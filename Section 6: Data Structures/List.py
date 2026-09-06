name = "Rahul"
age = 20

# What is a List 

# "A list is a collection of items
# stored in a single variable.

# Think of it like a shopping list —
# one list, multiple items!

# Lists in Python:
# ✅ Can store multiple values
# ✅ Items are ordered — have positions
# ✅ Items can be changed — mutable
# ✅ Can store different data types
# ✅ Items can be duplicated"

students=["Rahul","Priya","Amit","Sara","John","Priya"]
print(students)

marks=[85,78,95,88]
print(marks)

# list1=[]
# print(type(list1))

# list2=["X",1,5.4,True]
# print(list2)

# print(type(students))
# print(type(marks))

#indexing

students=["Rahul","Priya","Amit","Sara","John"]
print(students)

# print(len(students))

# print(students[1])
# print(students[4])

# print(students[-1])

# #slicing
# print(students[1:4:2])
# print(students[::2])
# print(students[::-1])

students=["Rahul","Priya","Amit","Sara","John"]
print(students)

# #change to item
# students[0]="rohan"
# print(students)

# #add item at end
# students.append("Neha")
# print(students)

# #remove
# students.remove("Amit")
# print(students)

# #sort
# students.sort()
# print(students)

# #check if item exist
# print("Priya" in students)
# print("Aisha" in students)

#for loop

students=["Rahul","Priya","Amit","Sara","John"]
print(students)

for student in students:
    print("Hello",student,"!")

#cal total marks

total=0
for mark in marks:
    total+=mark
print("Total marks",total)

