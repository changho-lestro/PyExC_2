menu = ""
student=[]


print("What would you like to do?")
print("\t[1] Show full gradebook")
print("\t[2] Add Student")
print("\t[3] Remove Student")
print("\t[4] Modify Student Information")
print("\t[5] Display Highest Grade")
print("\t[6] Display Lowest Grade")
print("\t[7] Quit")

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
        print(menu)

    elif menu == 4:
        print(menu)
        
    elif menu == 5:
        print(menu)
    elif menu == 6:
        print(menu)

    menu = int(input("Enter selection [1-7]"))

print("Terminating program... Goodbye!")
