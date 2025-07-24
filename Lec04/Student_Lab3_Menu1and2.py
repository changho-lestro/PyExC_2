menu = ""
student=[]

def show_menu():
    print("\n")
    print("What would you like to do?")
    print("\t[1] Show full gradebook")
    print("\t[2] Add Student")
    print("\t[3] Remove Student")
    print("\t[4] Modify Student Information")
    print("\t[5] Display Highest Grade")
    print("\t[6] Display Lowest Grade")
    print("\t[7] Quit")

def add_student():
    # prompt user for student name
    sname = input("Student Name?")
    # prompt user for student grade
    sgrade = int(input("Student Grade?"))

    return [sname, sgrade]


show_menu()
menu = int(input("Enter selection [1-7]"))

while menu != 7:
    if menu == 1:
        print("Name\tGrade")
        # loop through all students
        for s in student:
            print(s[0] + "\t" + str(s[1]))

    elif menu == 2:
        std_list =add_student()
        student.append(std_list)

    elif menu == 3:
        print(menu)

    elif menu == 4:
        print(menu)
        
    elif menu == 5:
        print(menu)
    elif menu == 6:
        print(menu)

    show_menu()
    menu = int(input("Enter selection [1-7]"))

print("Terminating program... Goodbye!")
