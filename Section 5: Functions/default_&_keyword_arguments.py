# def greet(name,greeting="Hello"):
#     print(greeting+ ","+name+"!")
# greet("Rahul")
# greet("Priya","Good morning")
# greet("Amit","Welcome")

#calculate price

# def calculate_price(amount,tax=18):
#     total=amount+(amount*tax/10)
#     return total

# price1=calculate_price(1000)
# print("price with default tax:"+str(price1))

# price2=calculate_price(2000,5)
# print("price with default tax:"+str(price2))

# # Profile creator
# def create_profile(name, age, city="Not specified"):
#     print("Name: " + name)
#     print("Age: " + str(age))
#     print("City: " + city)
#     print("-------------------")
# create_profile("Rahul", 22)
# create_profile("Priya", 21, "Hyderabad")


#keyword arguments

# Positional arguments
# def student_info(name, age, course):
#     print("Name: " + name)
#     print("Age: " + str(age))
#     print("Course: " + course)

# student_info("Rahul", 20, "BCA")
# student_info(course="BCA", age=20, name="Rahul")

# Ticket booking with keyword arguments

def book_ticket(passenger,destination,seat_type="Economy",meal="Veg"):
    print("Passenger : " + passenger)
    print("Destination: " + destination)
    print("Seat Type : " + seat_type)
    print("Meal      : " + meal)
    print("-------------------")

book_ticket(passenger="Syeda Munazza",destination="Mumbai",seat_type="Business",meal="Non veg")

book_ticket(passenger="Rahul",destination="Delhi")
    
    
