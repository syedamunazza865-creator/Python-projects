# with open("output.txt","w") as file:
#     file.write("We are learning file handling \n")
#     file.write("This is the 2nd file.\n")
#     file.write("Python file Handling is amazing!")
# print("File written successfully!")

# with open("output.txt","r") as file:
#     print(file.read())

# lines = [
#     "Rahul Kumar - 85%\n",
#     "Priya Sharma - 92%\n",
#     "Amit Singh - 78%\n"
# ]

# with open("results.txt","w") as file:
#     file.writelines(lines)
# print("REsults saved!")

# with open("results.txt", "r") as file:
#     print(file.read())

# with open("log.txt","w") as file:
#     file.write("Log file created! \n")
#     file.write("First entry added. \n")
# print("File created")

# with open("log.txt","a") as file:
#     file.write("second entry added!\n")
#     file.write("Third entry added. \n")
# print("Entries appended")

# with open("log.txt", "r") as file:
#     print(file.read())

# name=input("Enter your name:")
# msg=input("Enter your msg:")

# with open("msg.txt","a") as file:
#     file.write(f"Name: {name}| Message: {msg}")
# print("Message saved")
# print("\n All messages:")
# with open("msg.txt","r") as file:
#     print(file.read())

# File modes
modes = {
    "r": "Read — file must exist",
    "w": "Write — creates new or overwrites",
    "a": "Append — adds to existing file",
    
}

for mode, description in modes.items():
    print(f"'{mode}' mode: {description}")