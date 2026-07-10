import os
    
class MainMenu:

    def __init__(self, add_student, search_student, print_all_student):
        self.addstud = add_student
        self.search = search_student
        self.printAll = print_all_student

    def add_student_option(self):
        while True:
            os.system("clear")
            self.addstud.input_add_student()
            let = input("\nDo you want to add another student? (Y/N): ")
            if let.lower() != 'y':
                break

    def search_student_option(self):
        while True:
            os.system("clear")
            print("=" * 10, "Search Student Information", "=" * 10)
            key = input("\nEnter ID Number: ")
            print(self.search.search_student(key))
            let = input("\nDo you want to search another student? (Y/N): ")
            if let.lower() != 'y':
                break

    def main_menu(self, student):
        while True:
            os.system("clear")
            print(f"Welcome, {student[0]}!\n", "=" * 15, "Main Menu", "=" * 15)
            print("1. View your information\n2. View other students's information\n3. Register a new student\n4. Print all students in the list\n5. Exit")
            choice = input("\nEnter your choice: ")
            if choice == '1':
                os.system("clear")
                print(self.search.search_student(student[2]))
                input("Go back (Press Enter).")
            elif choice == '2':
                self.search_student_option()
            elif choice == '3':
                self.add_student_option()
            elif choice == '4':
                os.system("clear")
                self.printAll.print_all_students()
                input("Go back (Press Enter).")
            elif choice == '5':
                os.system("clear")
                print("=" * 10, "Logging off", "=" * 10, "\nLogging out. Goodbye.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

