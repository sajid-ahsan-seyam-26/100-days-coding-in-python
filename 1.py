student=[]
def add_student():
    print("---------add student----------")
    name=input("enter your name")
    id=input ("enter your id")
    roll=input("enter your roll")
    department=input("enter your dpartment name")
    phone=input("enter your phone number")

    student={

       "name": name,
        "roll": roll,
        "department": department,
        "phone": phone


    }
    student.append(student)
    print("your student added sucessfully")

    def show_all_shoudent():
        print("---all student print----")


