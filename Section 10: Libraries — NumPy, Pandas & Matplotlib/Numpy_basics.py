import numpy as np

# numbers=np.array([10,20,30,40,50])
# print("Array:",numbers)

# print("Type",type(numbers))
# print("Datatype:",numbers.dtype)

# zeros=np.zeros(5)
# print("Zeros:",zeros)

# ones=np.ones(5)
# print("Ones:",ones)

# range_array=np.arange(1,11)
# print("Range:",range_array)

# steps=np.arange(0,1.1,0.2)
# print("Steps:",steps)

# linespace=np.linspace(0,100,5)
# print("Linespace:",linespace)

marks=np.array([85,78,92,95,88])
print("original array:",marks)

# print("Add 5 to all:",marks+5)
# print("Multiply by 2",marks*2)
# print("percentage of 100:",marks/100*100)

# marks_list=[85,92,78,95,88]
# result=[]
# for mark in marks_list:
#     result.append(mark+5)
# print("List method:",result)

# print("NumPy method:", marks + 5)

# Mathematical functions
marks = np.array([85, 92, 78, 95, 88, 76, 91, 83])

# print("Mean (Average):", np.mean(marks))
# print("Median:", np.median(marks))
# print("Maximum:", np.max(marks))
# print("Minimum:", np.min(marks))
# print("Sum:", np.sum(marks))
# print("Standard Deviation:", np.std(marks))
# print("Sorted:", np.sort(marks))

print("First mark:",marks[0])
print("Last mark:",marks[-1])
print("Third mark:",marks[2])

print("First 3:",marks[:3])
print("Last 3:", marks[-3:])
print("Middle:", marks[2:6])

print("Marks above 85:",marks[marks>85])
print("Marks below 80:", marks[marks < 80])
print("Marks between 80-90:", marks[(marks >= 80) & (marks <= 90)])


# Practical example
student_marks = np.array([85, 42, 92, 38, 78, 55, 95, 29])

passed = student_marks[student_marks >= 35]
failed = student_marks[student_marks < 35]

print(f"Total students: {len(student_marks)}")
print(f"Passed: {len(passed)} students")
print(f"Failed: {len(failed)} students")
print(f"Class average: {np.mean(student_marks):.2f}%")
print(f"Highest mark: {np.max(student_marks)}")
print(f"Lowest mark: {np.min(student_marks)}")