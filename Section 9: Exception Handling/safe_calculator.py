print("========================================")
print("         SAFE CALCULATOR                ")
print("  Handles all errors gracefully!        ")
print("========================================")


class InvalidOperationError(Exception):
    pass


def calculate(num1, num2, operation):

    if operation == 1:
        return num1 + num2, "Addition"

    elif operation == 2:
        return num1 - num2, "Subtraction"

    elif operation == 3:
        return num1 * num2, "Multiplication"

    elif operation == 4:
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2, "Division"

    elif operation == 5:
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 % num2, "Modulus"

    else:
        raise InvalidOperationError(
            f"Invalid operation: {operation}"
        )


def get_number(prompt):

    while True:
        try:
            number = float(input(prompt))
            return number

        except ValueError:
            print("Invalid input! Please enter a number!")
            print("Letters and symbols are not allowed!\n")


def run_calculator():

    while True:

        print("\n========================================")
        print("         SELECT OPERATION               ")
        print("========================================")
        print("1. Addition       (+)")
        print("2. Subtraction    (-)")
        print("3. Multiplication (*)")
        print("4. Division       (/)")
        print("5. Modulus        (%)")
        print("6. Exit")
        print("========================================")

        choice = input("Enter Choice (1-6): ")

        if choice == "6":
            print("\nThank you for using Safe Calculator!")
            print("Goodbye! 👋")
            break

        try:

            # Convert choice from string to integer
            choice = int(choice)

            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            result, operation_name = calculate(
                num1,
                num2,
                choice
            )

            print("\n----------------------------------------")
            print(f"Operation  : {operation_name}")
            print(f"Numbers    : {num1} and {num2}")
            print(f"Result     : {result}")
            print("----------------------------------------")

        except ZeroDivisionError as e:

            print(f"\nMath Error: {e}")
            print("Please try again with different numbers!")

        except InvalidOperationError as e:

            print(f"\nOperation Error: {e}")
            print("Please select a valid operation (1-6)!")

        except ValueError:

            print("\nInput Error: Please enter a number from 1-6!")

        except Exception as e:

            print(f"\nUnexpected Error: {e}")
            print("Please try again!")

        finally:

            print("\nCalculation attempt complete!")


run_calculator()