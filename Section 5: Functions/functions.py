# print("Hello! Welcome!")
# print("Hello! Welcome!")
# print("Hello! Welcome!")
# print("Hello! Welcome!")
# print("Hello! Welcome!")

# A function is a block of reusable code
# that performs a specific task.
#inbuilt functions
# print()
# input()
# len()
# int()
# type()

#user defined
#defining functions
# def greeting():
#     print("Hello welcome to python")
#     print("Hope u are having a great day!")

# #calling
# greeting()
# greeting()

#show menu

# def print_line():
#     print("="*40)
# def show_menu():
#     print_line()
#     print("          Main Menu          ")
#     print_line()
#     print("1.Start game")
#     print("2.View score")
#     print("3.Exit")
#     print_line()
# show_menu()

# def wish_morning():
#     print("Good morning")
#     print("Have a productive dday")
# def wish_night():
#     print("Good night")
#     print("Sleep well")
# time=input("Is it morning or night?")

# if time=="morning":
#     wish_morning()
# else:
#     wish_night()

# Messy code — repeated everywhere
print("=" * 40)
print("Welcome!")
print("=" * 40)

# ... 50 lines later ...

print("=" * 40)
print("Welcome!")
print("=" * 40)

# ... 100 lines later ...

print("=" * 40)
print("Welcome!")
print("=" * 40)

# Clean code — define once use anywhere
def welcome():
    print("=" * 40)
    print("Welcome!")
    print("=" * 40)

welcome()
# ... 50 lines later ...
welcome()
# ... 100 lines later ...
welcome()