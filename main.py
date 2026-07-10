from add_student import AddStudent
from student import StudentInfo
from main_menu import MainMenu
from search_student import SearchStudent
from print_all_student import PrintAllStudent
import os

stu = StudentInfo()
addstud, search, printAll = AddStudent(stu), SearchStudent(stu), PrintAllStudent(stu)
menu = MainMenu(addstud, search, printAll)

attempts = 0
while attempts < 4:
    print("All data successfully added to the list")
    print("\n", "=" * 10, "Login - Student Info System", "=" * 10)
    
    login_check = input("Enter student ID to access the system: ")

    user = search.verify_login(login_check)
    if user:
        menu.main_menu(user)
        break
    else:
        attempts += 1
        print(f"\nThe student with the ID number {login_check} does not exist. \nAttempts left: {4 - attempts}")

if attempts >= 3:
    os.system("clear")
    print("=" * 7, "Login Error - Student Info System", "=" * 7)
    print("You have exceeded the number of attempts allowed.\nExiting the system. Goodbye.")
