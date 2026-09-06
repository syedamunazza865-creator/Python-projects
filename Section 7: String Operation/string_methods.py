#case methods

# text="hEllo wOrld pYthon"

# #upper
# print(text.upper())

# #lower
# print(text.lower())

# #title
# print(text.title())

# #capitalize()
# print(text.capitalize())

# #swapcase
# print(text.swapcase())

# name1=input("Enter your name:")
# name2="syeda munazza"

# if name1.lower()==name2.lower():
#     print("Names match")
# else:
#     print("Names dont match")

#cleaning methods
# text="   hello world   "
# print(text.strip())

# text="   hello world   "
# print(text.lstrip())

# text="   hello world   "
# print(text.rstrip())

# #replace

# msg="I love java programming!"
# print(msg.replace("java","python"))

# username=input("Enter username:")
# username=username.strip().lower()
# print("Cleaned username: ",username)

#searching methods

# sen="Python is the best programming language"

# print(sen.find("best"))

# #count
# print(sen.count("the"))
# print(sen.count("a"))

# # startswith() — checks beginning
# print(sen.startswith("Python"))
# print(sen.startswith("Java"))

# # # endswith() — checks ending
# # print(sen.endswith("language"))
# # print(sen.endswith("Python"))

# # in — check if substring exists
# print("best" in sen)
# print("Java" in sen)

#split()
sen="python is easy to learn"
words=sen.split()
print(words)

#split by specific char

date="2025-06-15"
parts=date.split("-")
print(parts)

print("Year:", parts[0])
print("Month:", parts[1])
print("Day:", parts[2])

#join()

words=["python","is","amazing"]
sen=" ".join(words)
print(sen)

