name = "Rahul"
age = 20
course = "BCA"
percentage = 85.5


# # Old way
# print("Name: " , name)
# print("Age: " , str(age))
# print("Percentage: " , str(percentage) + "%")

# #F-string way

# print(f"Name : {name}")
# print(f"Age : {age}")
# print(f"Course : {course}")
# print(f"Percentage : {percentage} %")

name="Syeda"
age=25

# print(f"Next year I will be {age+1} years old!")
# print(f"Name in uppercase: {name.upper()}")
# print(f"Name length : {len(name)} characters")

# #calculation

# marks=450
# total=500
# print(f"Percentage: {marks/total*100} %")

# #rounding numbers

# per=85.6789
# print(f"Percentage: {per:.2f} %")
# print(f"Percentage: {per:.1f} %")

# #number formatting
# salary=75000
# print(f"Salary: {salary:,}")
# print(f"Salary: {salary:,.2f}")

name = "Rahul Kumar"
roll = "BCA/2024/001"
course = "BCA"
semester = 3
marks = 456
total = 500
percentage = (marks/total) * 100

report = f"""
========================================
           STUDENT REPORT
========================================
Name       : {name}
Roll No    : {roll}
Course     : {course}
Semester   : {semester}
========================================
Marks      : {marks}/{total}
Percentage : {percentage:.2f}%
========================================
"""
print(report)