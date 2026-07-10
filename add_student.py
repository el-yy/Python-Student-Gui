from tkinter import messagebox

class AddStudent:
    def __init__(self, student_info):
        self.student_info = student_info

    def add_student(self, name, age, student_id, email, phone):
        # Validate inputs
        if not all([name, age, student_id, email, phone]):
            raise ValueError("All fields must be filled")

        # Check if student ID already exists
        self.student_info.read_file()
        if any(student[2] == student_id for student in self.student_info.all_students):
            raise ValueError(f"Student with ID {student_id} already exists")

        # Prepare student data
        new_student_data = f"{name}, {age}, {student_id}, {email}, {phone}\n"

        # Write to file
        with open("student_data.txt", "a") as file:
            file.write(new_student_data)

        # Update in-memory student list
        self.student_info.all_students.append([name, age, student_id, email, phone])

        # Optional: Show success message
        messagebox.showinfo("Success", f"Student {name} registered successfully!")