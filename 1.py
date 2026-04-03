student=[]
def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    department = input("Enter department: ")
    phone = input("Enter phone number: ")

    student = {
        "name": name,
        "roll": roll,
        "department": department,
        "phone": phone
    }

    students.append(student)

    print("Student added successfully.")


def show_all_students():
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No student data found.")
    else:
        count = 1
        for student in students:
            print("\nStudent", count)
            print("Name       :", student["name"])
            print("Roll       :", student["roll"])
            print("Department :", student["department"])
            print("Phone      :", student["phone"])
            count = count + 1


def search_student():
    print("\n--- Search Student ---")

    search_roll = input("Enter roll number to search: ")

    found = False

    for student in students:
        if student["roll"] == search_roll:
            print("\nStudent Found")
            print("Name       :", student["name"])
            print("Roll       :", student["roll"])
            print("Department :", student["department"])
            print("Phone      :", student["phone"])
            found = True
            break

    if found == False:
        print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    update_roll = input("Enter roll number to update: ")

    found = False

    for student in students:
        if student["roll"] == update_roll:
            print("Current Information:")
            print("Name       :", student["name"])
            print("Roll       :", student["roll"])
            print("Department :", student["department"])
            print("Phone      :", student["phone"])

            print("\nEnter new information")

            new_name = input("Enter new name: ")
            new_department = input("Enter new department: ")
            new_phone = input("Enter new phone number: ")

            student["name"] = new_name
            student["department"] = new_department
            student["phone"] = new_phone

            print("Student information updated successfully.")
            found = True
            break

    if found == False:
        print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    delete_roll = input("Enter roll number to delete: ")

    found = False

    for student in students:
        if student["roll"] == delete_roll:
            students.remove(student)
            print("Student deleted successfully.")
            found = True
            break

    if found == False:
        print("Student not found.")


def menu():
    while True:
        print("\n========== Student Management System ==========")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please try again.")


menu()
