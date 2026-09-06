print("==================")
print("Welcome to Python ATM")
print("==================")

correct_pin="1234"
bal=10000
attempts=0
max_attempts=3

while attempts<max_attempts:
    pin=input("\n Enter your pin:")

    if pin==correct_pin:
        print("Pin correct! Access granted")
        break
    else:
        attempts+=1
        remaining=max_attempts-attempts
        print("wrong pin")
        if remaining>0:
            print("Attempts remaining:"+str(remaining))
if attempts==max_attempts:
    print("\n card blocked, too many attempts")
    print("please viist your nearest branch")
else:
    print("\n========================================")
    print("      PYTHON ATM — MAIN MENU            ")
    print("========================================")
    print("Account Holder : Syeda Munazza")
    print("Account Number : XXXX XXXX 1234")
    print("Balance        : Rs." + str(bal))
    print("========================================")

    while True:
        print("\n please select an option")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Exit")

        choice=input("\n enter choice 1,2,3:")

        if choice=="1":
            print("---Balance enquiry-----")
            print("Available balance : Rs."+str(bal))
        elif choice=="2":
            print("-----cash withdrwal----")
            amount=int(input("Enter amount to withdraw:"))

            if amount <= 0:
                print("Invalid amount entered!")
                
            elif amount > bal:
                print("Insufficient balance!")
                print("Available balance: Rs." + str(bal))
                
            elif amount % 100 != 0:
                print("Please enter amount in multiples of 100!")
                
            else:
                bal = bal - amount
                print("Please collect your cash: Rs." + str(amount))
                print("Remaining balance: Rs." + str(bal))
                print("Thank you!")
        elif choice=="3":
             print("\nThank you for using Python ATM!")
             print("Please collect your card!")
             print("Goodbye! Have a great day! 👋")
             break
        else:
            print("Invalid choice! please enter 1,2 or 3:")