# "A dictionary stores data as
# key-value pairs.

# Every item has a KEY and a VALUE —
# just like a real dictionary has
# a WORD and its MEANING!

# student={
#     "name":"Rahul",
#     "age":20,
#     "course":"BCA",
#     "percentage":85.6,
#     "is_active":True
# }

# print(student)
# print(type(student))

# #accessing Dictionary
# print(student["name"])
# print(student["age"])
# print(student["course"])
# #print(student["city"])


# print(student.get("name"))
# print(student.get("city"))

#Modifying Dictionaries

# student={
#     "name":"Rahul",
#     "age":20,
#     "course":"BCA",
    
# }
# #updating existing value
# student["age"]=21
# print("updated age is:",student)

# #add new key-value pair
# student["city"]="Hyderabad"
# print("Added city:",student)

# #delete a key
# del student["course"]
# print("Deleted course:",student)


# #pop
# # pop() — removes and returns value
# student.pop("age")
# print("After pop:", student)

# #update multiple values at once
# student.update({"age": 22, "course": "MCA", "city": "Mumbai"})
# print("After update:", student)

#Dictinary methods
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA",
    "city": "Hyderabad"
}

#keys()
print(student.keys())

#values()
print(student.values())

#items()
print(student.items())
#loop through dictionary
for key in student:
    print(key+":"+str(student[key]))

#loop through items

for key,value in student.items():
    print(key+"-->"+str(value))


#check if key exists
print("name" in student)
print("Salary" in student)
print(len(student))