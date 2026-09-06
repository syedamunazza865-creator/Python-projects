# for i in range(1,6,2):
#     print(i)

count=1
while count<6:
     print(count)
     count+=1

#Guess a number
#--------------
# number=int(input("Guess the number:"))
# while number!=7:
#     print("wrong! try again")
#     number=int(input("Guess the number:"))
# print("correct!, you got it")

#password_checker
#----------------
# correct_pw="python123"
# attempts=0
# max_attempts=3

# while attempts<max_attempts:
#     p_w=input("Enter password")

#     if p_w==correct_pw:
#         print("Access granted! welcome")
#         break
#     else:
#         attempts+=1
#         remaning=max_attempts-attempts
#         print("Wrong password")
#         if remaning>0:
#             print("Attempts remaning",remaning)
# if attempts==max_attempts:
#     print("Account locked! too many wrong attempts")

#sum_calculator
#--------------

# total=0
# count=0

# print("Enter number to add:")
# print("Type 0 to stop")

# while True:
#     number=float(input("Enter a number:"))

#     if number==0:
#         break
#     total+=number
#     count+=1
# print("You entered"+ str(count)+"numbers")
# print("Total:"+str(total))

#Guess game
#----------

# secret=8
# guess=0
# attempts=0

# print("Guess the secret number:")

# while guess!=secret:
#     guess=int(input("Your guess?"))
#     attempts+=1

#     if guess<secret:
#         print("Too low, try higher")
#     elif guess>secret:
#         print("Too high, try lower")
#     else:
#         print("Correct! you got it right..")