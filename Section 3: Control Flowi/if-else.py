age=20
if age>=18:
    print("you are eligible to vote")
else:
    print("You are not yet eligible")

number=int(input("Enter a number:"))
if number%2==0:
    print(number," is even")
else:
    print(number,"is odd")

marks=int(input("Enter your marks:"))
if marks>=35:
    print("Congrtulations! you passed")
else:
    print("Sorry you failed,keep trying")

username=input("Enter username:")
password=input("Enter password:")

if username=="admin" and password=="python123":
    print("Login successful,welcome")
else:
    print("Invalid username and password")
