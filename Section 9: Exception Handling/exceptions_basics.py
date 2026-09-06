# print(10/0)

# #value error
# number=int("Hello")

# #Type error
# print("age"+20)

# # #Name error
# my_list=[1,2,3]
# # print(mylist)

# #Index error
# print(my_list[5])

# try:
#     number=int(input("Enter a number:"))
#     result=10/number
#     print("Result:",result)
# except ValueError:
#     print("Invalid input ! plz enter a number.")
# except ZeroDivisionError:
#     print("Cannot divide with zero")

try:
    age = int(input("Enter your age: "))
    
    if age < 0:
        print("Age cannot be negative!")
    else:
        print(f"You are {age} years old!")
        print(f"In 10 years you will be {age + 10}!")

except ValueError:
    print("Please enter a valid number for age!")

# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
else:
    print("No errors occured")
