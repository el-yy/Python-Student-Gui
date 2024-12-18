class PrintAllStudent:
    def __init__(self, student_info):
        self.student_info = student_info

    def print_all_students(self):
        if not self.student_info.allstudents:
            print("\nNo students found.")
            return
        
        print("\n==================== All Students' Information ====================")
        for student in self.student_info.allstudents:
            name, age, idnum, email, phone = student
            print(f"Name: {name}\nAge: {age}\nStudent ID: {idnum}\nEmail: {email}\nPhone: {phone}\n")
        print("==================== Nothing Follows ====================")
        return
