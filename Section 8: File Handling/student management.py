Students=[]
while True:
    print("\nStudent Management System")
    print("1. Add Student Details")
    print("2. View All Students")
    print("3. Update Student Details")
    print("4. Delete Student Details")
    print("5. Quit")

    choice = int(input("Enter your choice: "))

    # Add student details
    if choice == 1:
      num_students = int(input("Enter the number of students to add: "))
      for i in range(num_students):
          name = input("Enter student {}'s name: ".format(i+1))
          age = int(input("Enter student {}'s age: ".format(i+1)))
          grade = float(input("Enter student {}'s grade: ".format(i+1)))
          details= [name, age, grade]
          Students.append(details)
      print("Student details added successfully.")

    # View all students
    elif choice == 2:
        print("Student Details:")
        for student in Students:
          print("Name:", student[0])
          print("Age:", student[1])
          print("Grade:", student[2])
          print()

    # Update student details
    elif choice == 3:
        name = input("Enter the student's name to update: ")
        for student in Students:
            if student[0] == name:
                age = int(input("Enter the new age: "))
                grade = float(input("Enter the new grade: "))
                student[1] = age
                student[2] = grade
                print("Student details updated successfully.")
                break
        else:
            print("Student not found.")

    # Delete student details
    elif choice == 4:
        name = input("Enter the student's name to delete: ")
        for student in Students:
            if student[0] == name:
                Students.remove(student)
                print("Student details deleted successfully.")
                break
        else:
            print("Student not found.")

    # Quit the program
    elif choice == 5:
        print("Exiting...")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please try again.")
