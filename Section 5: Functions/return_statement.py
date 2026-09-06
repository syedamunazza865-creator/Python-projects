# def add(a,b):
#     return a+b
# result=add(5,3)
# print(result)

#square function with return

# def square(number):
#     return number*number
# result=square(5)
# print("square of 5 is:",result)

# #calculating percentage

# def cal_per(marks,total):
#     per=(marks/total)*100
#     return per

# percent=cal_per(450,500)
# print("Percentage:"+str(percent)+"%")

# #grade function

# def get_grade(percentage):
#     if percentage>=90:
#         return "A+"
#     elif percentage>=80:
#         return "A"
#     elif percentage>=70:
#         return "B+"
#     elif percentage>=60:
#         return "B"
#     elif percentage>=35:
#         return "C"
#     else:
#         return "F"
    
# grade=get_grade(85)
# print("Grade:"+grade)

#check_number

# def check_num(num):
#     if num>0:
#         return "positive"
#     elif num<0:
#         return "negative"
#     else:
#         return "zero"
#     print("This will never run!")

# result=check_num(5)
# print(result)

#combining functions

def get_total(marks_list):
    total = 0
    for mark in marks_list:
        total += mark
    return total

def get_percentage(total, max_marks):
    return (total / max_marks) * 100

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 35:
        return "C"
    else:
        return "F"

# Use all functions together
maths = int(input("Enter maths marks: "))
science = int(input("Enter science marks: "))
english = int(input("Enter english marks: "))

marks = [maths, science, english]
total = get_total(marks)
percentage = get_percentage(total, 300)
grade = get_grade(percentage)

print("Total    : " + str(total))
print("Percentage: " + str(round(percentage, 2)) + "%")
print("Grade    : " + grade)