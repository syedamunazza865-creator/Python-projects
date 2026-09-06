# for i in range(1,16,2):
#     print(i)

#backward loop-->20-1
# for count in range(20,0,-2):
#     print(count)

# #sum of numbers
# total=0
# for i in range(1,101):
#     total=total+i
# print("sum of 1 to 100:",str(total))

# #Multiplication table
# num=int(input("Enter a number:"))
# for i in range(1,11):
#     result=num*i
#     print(str(num)+"x"+str(i)+"="+str(result))

# name="Python"
# for letter in name:
#     print(letter)

word=input("Enter a word:")
vowels="aeiouAEIOU"
count=0

for letter in word:
    if letter in vowels:
        count=count+1
print("Number of vowels:"+str(count))