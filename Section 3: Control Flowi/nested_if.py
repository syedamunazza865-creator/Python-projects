# age=19
# has_id=False

# if age>=18:
#     print("Age requirement met!")

#     if has_id==True:
#         print("ID verified")
#         print("Entry allowed!")
#     else:
#         print("No ID found!")
#         print("Entry not allowed")
# else:
#     print("Too young!,Entry not allowed")

#Shopping discount System
#------------------------

customer_name=input("Enter your name:")
member_type=input("Are you a member? (yes/no):")

if member_type=="yes":
    print("Welcome member",customer_name,"!")
    purchase=float(input("Enter purchase amount in rupees:"))

    if purchase>=5000:
        discount=purchase*0.20
        print("Wow! you get 20% discount!")
        print("Discount amount:",str(discount))
        print("Final amount:",str(purchase-discount))
    elif purchase>=2000:
        discount=purchase*0.10
        print("Wow! you get 10% discount!")
        print("Discount amount:",str(discount))
        print("Final amount:",str(purchase-discount))
    else:
        print("Minimum 2000 rupeespurchase needed for discount!")
        print("Total amount:",str(purchase))
else:
    print("Hello",customer_name,"!")
    purchase=float(input("Enter purchase amount in rupees:"))
    if purchase>=5000:
        discount=purchase*0.05
        print("Wow! you get 5% discount!")
        print("Final amount:",str(purchase-discount))
    else:
        print("No discount available!")
        print("Total amount:",str(purchase))
    print("Tip: Become a member for bigger discounts")
