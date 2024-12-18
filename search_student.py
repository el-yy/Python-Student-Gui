class SearchStudent:
    def __init__(self, student_info):
        # Ensure we reference the allstudents list from StudentInfo
        self.students = student_info.all_students

    def search_student(self, keyword):
        for student in self.students:
            if student[2] == keyword:
                return f"Name: {student[0]}\nAge: {student[1]}\nStudent ID: {student[2]}\nEmail: {student[3]}\nPhone: {student[4]}"
        return "Student not found."

    def verify_login(self, student_id):
        # Loop through students and match the ID
        for student in self.students:
            if student[2] == student_id:
                return student
        return False
