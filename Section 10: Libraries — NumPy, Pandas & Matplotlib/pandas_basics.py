# Series:          DataFrame:
# Name             Name    Age    Course
# Rahul            Rahul   20     BCA
# Priya            Priya   22     BTech
# Amit             Amit    21     BSc

# import pandas as pd
# import numpy as np

# marks=pd.Series([85,92,78,95,88])
# print("Basics Series")
# print(marks)
# print()

# marks=pd.Series([85,92,78,95,88],index=["Rahul","Priys","Amit","Sra","John"])
# print("Series with names:")
# print(marks)
# print()
# print("Above 85:",marks[marks>85])

# print("Rahul's marks:",marks["Rahul"])

# print("Mean:", marks.mean())
# print("Max:", marks.max())
# print("Min:", marks.min())


import pandas as pd
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sara", "John"],
    "Age": [20, 22, 21, 23, 20],
    "Course": ["BCA", "BTech", "BSc", "BCA", "BTech"],
    "Percentage": [85.5, 92.0, 78.5, 88.0, 95.5]
}
df=pd.DataFrame(data)
print(df)
print()

print("Shape:",df.shape)
print(df.columns.tolist())
print("Size:",df.size)

print("First 3 rows:")
print(df.head(3))

print("Last 3 rows:")
print(df.tail(3))

print("\n DataFrame info:")
print(df.info())

print("\n Statistics:")
print(df.describe())

print("All names and percentage:")
print(df[["Name","Percentage"]])

print("\n First studnet:")
print(df.iloc[0])
print("\n Student at index 2:")
print(df.iloc[2])

print("\n Btech students:")
print(df[df["Course"]=="BTech"])

print("\nStudents above 85%:")
print(df[df["Percentage"] > 85])

df["Grade"]=df["Percentage"].apply(lambda x:"A" if x>=90 else "B" if x>=80 else "C")
print(df)

# Basic statistics on column
print("\nPercentage Statistics:")
print(f"Average: {df['Percentage'].mean():.2f}%")
print(f"Highest: {df['Percentage'].max()}%")
print(f"Lowest : {df['Percentage'].min()}%")
