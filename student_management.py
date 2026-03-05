import json

List = []

def Students():

    while True:

        while True:
            try:
                Student_ID = int(input("Enter student ID: "))
            except ValueError:
                print("ID must be a number. Try again")
                continue

            for student in List:
                if student["ID"] == Student_ID:
                    print("Student ID already exists")
                    break
                
            else:
                break

        Student_Name = input("Enter student name: ")    
        
        while True:
            try:
                Student_Age = int(input("Enter student age: "))
                break
            except ValueError:
                print("Age must be a number. Try again")
            

        while True:
            try:
                Student_Grade = int(input("Enter student grade: "))
                break
            except ValueError:
                print("Grade must be a number. Try again")
                


        Add_Student = {

            "ID":Student_ID,
            "Name":Student_Name,
            "Age":Student_Age,
            "Grade":Student_Grade

        }
        List.append(Add_Student)

        another = input("Add another student?: (y/n): ").strip().lower()
        if another =="n":
            break

        
def update_student():
    update_id = int(input("Enter the ID of the student to update: "))

    for student in List:
        if update_id == student["ID"]:
            new_name = input("Enter new name (current: " + student["Name"] + "): ")
            if new_name.strip() != "":
                student["Name"] = new_name.strip()
        
            new_age = input("Enter new age(current: " + str(student["Age"]) + "): " )
            if new_age.strip() != "":
                try:
                    student["Age"] = int(new_age)
                except ValueError:
                    print("Invalid input.")
            
            new_grade = input("Enter new grade(current: " + str(student["Grade"]) + "): ")
            if new_grade.strip() != "":
                try:
                    student["Grade"] = int(new_grade)
                except ValueError:
                    print("Invalid input")
        
            print("Student updated successfully!")
            break
    else:
        print("Student not found.")


def delete_student():
    while True:
        try:
            delete_id = int(input("Enter the ID of the student to delete: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers only")

    for student in List:
        if delete_id == student["ID"]:
            List.remove(student)
            print("Student successfully deleted!")
            break
    else:
        print("Student not found.")

def view_Students():
    if List == []:
        print("No students found.")
    else:
        for student in List:
            print(student)

def save_and_exit():
    with open("students.json","w") as f:
        json.dump(List, f, indent=4)


def main():
    while True:

        print("---Student Management System---")
        print("1.Add Student\n" \
        "2.View Students\n" \
        "3.Update Student\n" \
        "4.Delete Student\n" \
        "5.Save & Exit")
        
        option = input("Please enter option number: ").strip()


        if option == "1":
            Students()
        elif option == "2":
            view_Students()
        elif option == "3":
            update_student()
        elif option == "4":
            delete_student()
        elif option == "5":
            save_and_exit()
            break
        else:
            print("Invalid option. Please try again.")

main()







