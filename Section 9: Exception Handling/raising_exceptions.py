# Section 9 - Video 3
# Raising Exceptions & Custom Errors

# Raising built-in exceptions
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age cannot be more than 150!")
    print(f"Age set to: {age}")

try:
    set_age(-5)
except ValueError as e:
    print(f"Error: {e}")

try:
    set_age(200)
except ValueError as e:
    print(f"Error: {e}")

try:
    set_age(25)
except ValueError as e:
    print(f"Error: {e}")

# Type checking with isinstance
def set_percentage(percentage):
    if not isinstance(percentage, (int, float)):
        raise TypeError("Percentage must be a number!")
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be between 0 and 100!")
    print(f"Percentage: {percentage}%")

try:
    set_percentage("85")
except TypeError as e:
    print(f"Type Error: {e}")

try:
    set_percentage(150)
except ValueError as e:
    print(f"Value Error: {e}")

# Custom exceptions
class InvalidAgeError(Exception):
    pass

class InvalidPercentageError(Exception):
    pass

def add_student(name, age, percentage):
    if age < 0 or age > 100:
        raise InvalidAgeError(f"Invalid age: {age}!")
    if percentage < 0 or percentage > 100:
        raise InvalidPercentageError(f"Invalid percentage: {percentage}!")
    if not name:
        raise ValueError("Name cannot be empty!")
    print(f"Student added: {name}, {age}, {percentage}%")

try:
    add_student("Rahul", -5, 85)
except InvalidAgeError as e:
    print(f"Age Error: {e}")

try:
    add_student("Priya", 20, 150)
except InvalidPercentageError as e:
    print(f"Percentage Error: {e}")

try:
    add_student("", 20, 85)
except ValueError as e:
    print(f"Value Error: {e}")

try:
    add_student("Amit", 20, 85)
except (InvalidAgeError, InvalidPercentageError, ValueError) as e:
    print(f"Error: {e}")