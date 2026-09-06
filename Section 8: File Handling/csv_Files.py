# import csv

# with open("students.csv","r") as file:
#     reader=csv.reader(file)

#     for row in reader:
#         print(row)

# import csv
# with open("students.csv","r") as file:
#     reader=csv.reader(file)

#     header=next(reader)
#     print("Headers:",header)
#     print("="*40)

#     for row in reader:
#         name=row[0]
#         course=row[1]
#         per=row[2]
#         print(f"Name: {name} | Course: {course} | Percentage: {percentage}%")

#DictReader

# import csv

# with open("students.csv","r") as file:
#     reader=csv.DictReader(file)
    
#     for row in reader:
#         print(f"Name: {row['Name']}")
#         print(f"Course: {row['Course']}")
#         print(f"Percentage: {row['Percentage']}%")
#         print("---")

#writing in csv file
import csv
students = [
    ["Name", "Course", "Percentage"],
    ["Rahul Kumar", "BCA", 85.5],
    ["Priya Sharma", "BTech", 92.0],
    ["Amit Singh", "BSc", 78.5],
    ["Sara Khan", "BCA", 88.0]
]
with open("new_students.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(students)
print("csv file created")

with open("new_students.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#appending 
import csv

# Add new student to existing CSV
new_student = ["John Mathew", "BTech", 95.5]

with open("new_students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_student)

print("New student added!")

# Verify
with open("new_students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)