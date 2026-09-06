# "Matplotlib allows us to create:

# 📈 Line Charts — show trends over time
# 📊 Bar Charts — compare categories
# 🥧 Pie Charts — show percentages
# 📉 Scatter Plots — show relationships
# 📦 Histograms — show distributions

import matplotlib.pyplot as plt
import numpy as np


# # Student marks over 6 months
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# marks = [65, 70, 68, 75, 80, 85]
# plt.figure(figsize=(10,6))
# plt.plot(months,marks,color="blue",marker="o",linewidth=2,markersize=8,label="Rahul's marks")
# plt.title("Student Performance Over 6 Months", fontsize=16)
# plt.xlabel("Month",fontsize=12)
# plt.ylabel("Marks",fontsize=12)
# plt.legend()
# plt.grid(False)
# plt.ylim(0,100)
# plt.show()
# students = ["Rahul", "Priya", "Amit", "Sara", "John"]
# marks = [85, 92, 78, 88, 95]
# colors = ["blue", "green", "red", "orange", "purple"]
# plt.figure(figsize=(10,6))
# plt.bar(students,marks,color=colors,width=0.5,edgecolor="black")
# plt.title("Student marks comparision",fontsize=16)
# plt.xlabel("Students", fontsize=12)
# plt.ylabel("Marks", fontsize=12)
# plt.ylim(0, 100)

# for i,mark in enumerate(marks):
#     plt.text(i,mark+1,str(mark),ha="center",fontsize=11)
# plt.grid(axis="y",alpha=0.3)
# plt.show()

# # Course distribution
# courses = ["BCA", "BTech", "BSc", "MBA"]
# students = [35, 45, 20, 15]
# colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]
# explode = (0, 0.2, 0, 0)  # explode BTech slice

# plt.figure(figsize=(8,8))
# plt.pie(students,labels=courses,colors=colors,explode=explode,autopct="%1.1f%%",shadow=True,startangle=90)
# plt.title("Student course Distribution",fontsize=16)
# plt.legend(courses,loc="upper right")
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Student data
students = ["Rahul", "Priya", "Amit", "Sara", "John"]
marks = [85, 92, 78, 88, 95]
months = ["Jan", "Feb", "Mar", "Apr", "May"]
monthly_avg = [72, 75, 78, 82, 87]

# Create figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1 — Bar chart
ax1.bar(students, marks, color="steelblue", edgecolor="black")
ax1.set_title("Student Marks", fontsize=14)
ax1.set_xlabel("Students")
ax1.set_ylabel("Marks")
ax1.set_ylim(0, 100)

# Plot 2 — Line chart
ax2.plot(months, monthly_avg, 
         color="green", marker="o", linewidth=2)
ax2.set_title("Monthly Average", fontsize=14)
ax2.set_xlabel("Month")
ax2.set_ylabel("Average Marks")
ax2.set_ylim(0, 100)
ax2.grid(True)

plt.suptitle("Student Performance Dashboard", 
             fontsize=16, fontweight="bold")
plt.tight_layout()
plt.show()

