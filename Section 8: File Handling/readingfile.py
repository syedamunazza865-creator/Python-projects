# file=open("students.txt","r")
# content=file.read()
# print(content)
# file.close()

# with open("students.txt","r") as file:
#     content=file.read()
#     print(content)

#reading line by line

with open("students.txt","r") as file:
    line1=file.readline()
    line2=file.readline()
    print("Line 1:",line1)
    print("Line 2:",line2)

#readlines()

with open("students.txt","r") as file:
    print("All students:")
    print("="*40)
    for line in file:
        line=line.strip()
        print(line)