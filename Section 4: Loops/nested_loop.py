# for i in range(1,4):
#     for j in range(1,4):
#         print("i="+str(i)+"j="+str(j))
#     print("Inner loop done for i="+str(i))

#printing patterns
#-----------------

# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print

#triangle pattern
#----------------

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

#Multiplication table
#--------------------

print("Multiplication tables")
print("=====================")

for i in range(1,4):
    print("\n Table of"+str(i)+":")
    print("-----------------------")

    for j in range(1,11):
        result=i*j
        print(str(i)+"x"+str(j)+"="+str(result))