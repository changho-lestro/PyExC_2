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
        rm_stdt = input("Student to remove?")
        idx_num = 0
        for s in student:
            if rm_stdt == s[0]:
                student.pop(idx_num)
                print("Removed.")
            else:
                idx_num += 1
        if idx_num == len(student):
            print("Your input is invalid.")

    elif menu == 4:
        mod_flag = False
        mod_stdt = input("Student to modify?")
        idx_num = 0
        for s in student:
            if mod_stdt == s[0]:
                mod_flag = True
                print(s[0] + "\t" + str(s[1]))
                nmtoMod = input("Name: (press Enter to keep original value)")
                grdtoMod = input("Grade: (press Enter to keep original value)")

                if nmtoMod != "":
                    student[idx_num][0] = nmtoMod
                if grdtoMod != "":
                    student[idx_num][1] = int(grdtoMod)
                print("Saved.")
            else:
                idx_num += 1
        if not mod_flag:
            print("Not found.")

    elif menu == 5:
        print(menu)
    elif menu == 6:
        print(menu)

    menu = int(input("Enter selection [1-7]"))

print("Terminating program... Goodbye!")
