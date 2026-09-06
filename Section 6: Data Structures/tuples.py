# A tuple is an ordered collection
# of items — just like a list.

# But the key difference is —
# Tuples are IMMUTABLE!

# Immutable means — once created,
# they CANNOT be changed!

# List — uses square brackets
# students_list = ["Rahul", "Priya", "Amit"]

# # Tuple — uses round brackets
# students_tuple = ("Rahul", "Priya", "Amit")

# print(type(students_list))
# print(type(students_tuple))

students_list = ["Rahul", "Priya", "Amit"]
students_tuple = ("Rahul", "Priya", "Amit")
# students_list[0]="Rohan"
# print(students_list)
# students_tuple[0]="Rohan"
# print(students_tuple)

#accessing tuples

# cordinates=(10.5,20.5,60.7,85.6,96.6)

# print(cordinates[0])
# print(cordinates[-1])
# #slicing
# print(cordinates[2:4])
# print(cordinates[::-1])

colors = ("red", "green", "blue", "red", "yellow")

# # count — how many times item appears
# print(colors.count("red"))   # 2

# # index — position of item
# print(colors.index("blue"))  # 2

# # Check if item exists
# print("green" in colors)     # True
# print("pink" in colors)      # False

# Days of week — never changes!
days = ("Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday")

# RGB color values — fixed!
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# GPS coordinates — fixed point!
location = (17.3850, 78.4867)  # Hyderabad coordinates!

