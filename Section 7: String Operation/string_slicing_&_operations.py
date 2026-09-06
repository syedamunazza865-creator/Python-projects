# text="Python"

# print(text[0])
# print(text[1])
# print(text[2])
# print(text[5])

# #negative index

# print(text[-1])
# print(text[-2])
# print(text[-6])

# #string slicing
# text1="python programming"

# print(text1[0:6])
# print(text1[7:18])

# print(text1[::2])
# # print(text1[::-1])

# email="syeda@gmail.com"
# username=email[:email.find("@")]
# print("Username: ",username)

# domain=email[email.find("@")+1:]
# print("Doamin: ",domain)

# print("Is valid", "@" in email and "." in email)

#string opertions

print("="*40)
print("python"*3)

#concatenation
fname="syeda"
lname="munazza"
fullname=fname+" "+lname
print(fullname)

#check string content
text2="python123"
print(text2.isalpha())
print(text2.isdigit())
print(text2.isalnum())
print(text2.isspace())

#string alignment
text3="Python"
print(text3.center(20,"*"))
print(text3.ljust(20,"-"))
print(text3.rjust(20,"-"))