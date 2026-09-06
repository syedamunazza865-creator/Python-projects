# students = ["Rahul", "Priya", "Amit"]

# #add items

# #append

# students.append("Sara")
# print(students)

# #insert
# students.insert(1,"John")
# print(students)

# #extend
# new_students=["Neha","Ravi"]
# students.extend(new_students)
# print(students)

# # append vs extend
# list1 = [1, 2, 3]
# list1.append([4, 5])
# print("append:", list1)

# list2 = [1, 2, 3]
# list2.extend([4, 5])
# print("extend:", list2)

#removing items

# students = ["Rahul", "Priya", "Amit", "Sara"]

# #remove
# students.remove("Priya")
# print(students)

# #pop
# students.pop()
# print(students)

# #clear
# students.clear()
# print(students)


#oragnize list

numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print("Original:", numbers)

#sort
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

#reverse
numbers.reverse()
print(numbers)

# Sorting strings
names = ["Rahul", "Amit", "Priya", "John", "Sara"]
names.sort()
print("Sorted names:", names)

#index

print(names.index("Amit"))

# count() - counts occurrences

marks = [85, 92, 85, 78, 85, 92]
print("85 appears:", marks.count(85), "times")
print("92 appears:", marks.count(92), "times")

# copy() - creates a copy of list
original = [1, 2, 3, 4, 5]
copied = original.copy()
copied.append(6)
print("Original:", original)
print("Copied:", copied)

