# "A set is a collection of
# unique unordered items.

# Key features of sets:

# No duplicate values allowed
# Items have no fixed order
# Very fast for checking membership

fruits={"apple","banana","mango","orange","apple"}
# print(fruits)
# print(type(fruits))

# #create set from list
# students=["Rahul","Priya","Amit","John","Rahul"]
# unique_students=set(students)
# print(unique_students)

#Adding and Removing


fruits={"apple","banana","mango","orange","apple"}
# fruits.add("Kiwi")
# print(fruits)

#update
# fruits.update(["grapes","chickoo"])
# print("After update:",fruits)

# #remove
# fruits.remove("guava")
# print("Afer removing:",fruits)

# #discard
# fruits.discard("guava")
# print("Afer removing:",fruits)

# #pop
# print(fruits.pop())

# #clear()
# fruits.clear()
# print(fruits)

# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}

# #union
# print(set_a|set_b)
# print(set_a.union(set_b))

# #intersection

# print(set_a&set_b)
# print(set_a.intersection(set_b))

# #differnce

# print(set_a-set_b)

# #check if item exits
# print(3 in set_a)
# print(9 in set_b)


python_students = {"Rahul", "Priya", "Amit", "Sara"}
java_students = {"Amit", "John", "Sara", "Neha"}

# Students in both courses
both = python_students & java_students
print("In both courses:", both)

#Students in python
python_only = python_students - java_students
print("Python only:", python_only)

# All unique students
all_students = python_students | java_students
print("All students:", all_students)