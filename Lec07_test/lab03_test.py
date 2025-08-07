# Lab 03
# Ahmed Kadar
# 7/17/2025
# Functions & Classes

menu = ""
student=[]

def show_menu():
    print("What would you like to do?")
    print("\t[1] Show full gradebook")
    print("\t[2] Add Student")
    print("\t[3] Remove Student")
    print("\t[4] Modify Student Information")
    print("\t[5] Display Highest Grade")
    print("\t[6] Display Lowest Grade")
    print("\t[7] Quit")

show_menu()
menu = int(input("Enter selection [1-7]"))

while menu != 7:
    if menu == 1:
        print("Name\tGrade")
        # loop through all students
        for s in student:
            print(s[0] + "\t" + str(s[1]))

    elif menu == 2:
        # prompt user for student name
        sname = input("Student Name?")
        # prompt user for student grade
        sgrade = int(input("Student Grade?"))
        # append student information to list
        student.append([sname,sgrade])

    elif menu == 3:
        del_name = input("Enter the name of the student to remove: ")
        # find the student in the list and remove them
        for s in student: # loop through all students
            if s[0] == del_name: # check if the name matches
                student.remove(s) # remove the student
                print(f"Removed {del_name} from the gradebook.")
                break
        else: # if no break occurred, the student was not found
            print(f"Student {del_name} not found in the gradebook.") # if no student was removed
        print(menu)

    elif menu == 4:
        mod_name = input("Enter the name of the student to modify: ")
        for s in student:
            if s[0] == mod_name:
                new_name = input("Enter new name: ")
                new_grade = int(input("Enter new grade: "))
                s[0] = new_name
                s[1] = new_grade
                print(f"Modified {mod_name} to {new_name} with grade {new_grade}.")
                break
        print(menu)
    elif menu == 5:
        highest = max(student, key=lambda x: x[1]) # find the student with the highest grade
        print(f"Highest Grade: {highest[0]} with a grade of {highest[1]}") # display the highest grade and student name
        print(menu)
    elif menu == 6:
        lowest = min(student, key=lambda x: x[1]) # find the student with the lowest grade
        print(f"Lowest Grade: {lowest[0]} with a grade of {lowest[1]}") # display the lowest grade and student name
        print(menu)
    else:
        print("Invalid selection. Please try again.")
        show_menu()
    menu = int(input("Enter selection [1-7]"))
print("Terminating program... Goodbye!")
