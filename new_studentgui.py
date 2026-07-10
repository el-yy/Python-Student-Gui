from tkinter import *
from functools import partial
from add_student import AddStudent
from student import StudentInfo
from search_student import SearchStudent
from tkinter import ttk

student_info = StudentInfo()
add_student_handler = AddStudent(student_info)
search_handler = SearchStudent(student_info)
login_attempts = 5

win = Tk()
win.title("Student Management System")
win.configure(bg="#121212")

style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", 
    background="#2E2E2E", foreground="#FFFFFF", font=("Arial", 12), padding=10
)
style.configure("TLabel", 
    background="#121212", foreground="#FFFFFF", font=("Arial", 12)
)
style.configure("TEntry", 
    background="#1E1E1E", foreground="#FFFFFF", fieldbackground="#1E1E1E"
)

login_div = Frame(win, bg="#121212")
main_div = Frame(win, bg="#121212")
menu_div = Frame(main_div, bg="#2E2E2E")
info_div = Frame(main_div, bg="#121212")
search_div = Frame(main_div, bg="#121212")
register_div = Frame(main_div, bg="#121212")
studentList_div = Frame(main_div, bg="#121212")

def switch_frame(frame_to_show):
    for frame in [info_div, search_div, register_div, studentList_div]:
        frame.pack_forget()
    frame_to_show.pack(side="left", fill="both", expand=True)

def login():
    global login_attempts
    student_id = student_id_entry.get()
    student_info.read_file()

    for student in student_info.all_students:
        if student_id == student[2]:
            login_div.pack_forget()
            main_div.pack(side="left", fill="both", expand=True)
            menu_div.pack(side="left", fill="y")
            show_student_info(student)
            return

    login_attempts -= 1
    if login_attempts > 0:
        login_status_label.config(text=f"Invalid Student ID. {login_attempts} attempts remaining.", foreground="#CF6679")
    else:
        login_status_label.config(text="Too many failed attempts. Exiting the program.", foreground="#CF6679")
        win.quit()

def logout():
    global login_attempts
    login_attempts = 5
    student_id_entry.delete(0, END)
    main_div.pack_forget()
    login_div.pack(side="left", fill="both", expand=True)

def create_login_screen():
    global student_id_entry, login_status_label
    login_container = Frame(login_div, bg="#121212")
    login_container.place(relx=0.5, rely=0.5, anchor=CENTER)
    ttk.Label(
        login_container, 
        text="Student Management System", font=("Arial", 24, "bold")
    ).pack(pady=(0, 30))
    ttk.Label(
        login_container, 
        text="Enter Student ID:", font=("Arial", 14)
    ).pack(pady=5)
    student_id_entry = ttk.Entry(
        login_container, 
        width=30, font=("Arial", 12)
    )
    student_id_entry.pack(pady=10)
    login_button = ttk.Button(
        login_container, 
        text="Login", command=login, style="TButton"
    )
    login_button.pack(pady=20)
    login_status_label = ttk.Label(
        login_container, 
        text="",  font=("Arial", 12)
    )
    login_status_label.pack(pady=10)
def show_student_info(student):
    display_info(info_div, "Student Information", student)
def display_info(frame, title, student):
    for widget in frame.winfo_children():
        widget.destroy()
    ttk.Label(
        frame, text=title, font=("Arial", 20, "bold")
    ).pack(pady=20)
    info_frame = Frame(frame, bg="#121212")
    info_frame.pack(expand=True)
    fields = [
        ("Name:", student[0]), 
        ("Age:", student[1]), 
        ("Student ID:", student[2]), 
        ("Email:", student[3]), 
        ("Phone:", student[4])
    ]
    for label_text, value in fields:
        row_frame = Frame(info_frame, bg="#121212")
        row_frame.pack(fill='x', padx=50, pady=5) 
        ttk.Label(
            row_frame, 
            text=label_text, width=15, anchor='e', font=("Arial", 14, "bold")
        ).pack(side=LEFT, padx=10)
        ttk.Label(
            row_frame, text=value, width=30, anchor='w', font=("Arial", 14)
        ).pack(side=LEFT)
def show_search_result(student, result_frame):
    display_info(result_frame, "Search Result", student)
def create_main_menu():
    menu_container = Frame(menu_div, bg="#2E2E2E")
    menu_container.pack(fill='both', expand=True)
    ttk.Label(
        menu_container, 
        text="Main Menu", font=("Arial", 18, "bold"), background="#2E2E2E", foreground="#FFFFFF"
    ).pack(pady=20)
    btn_config = [
        ("My Info", info_div), 
        ("Search", search_div), 
        ("Register", register_div), 
        ("View All", studentList_div), 
        ("Logout", None)
    ]
    for text, frame in btn_config:
        btn = ttk.Button(
            menu_container, 
            text=text, style="TButton", command=partial(switch_frame, frame) if frame else logout
        )
        btn.pack(pady=10, padx=20, fill='x')
def create_search_section():
    search_form_frame = Frame(search_div, bg="#121212")
    search_form_frame.pack(pady=20)
    ttk.Label(
        search_form_frame, 
        text="Search Student", font=("Arial", 20, "bold")
    ).pack(pady=20)
    ttk.Label(
        search_form_frame, 
        text="Enter Student ID:", font=("Arial", 14)
    ).pack(pady=5)
    search_entry = ttk.Entry(
        search_form_frame, 
        width=30, font=("Arial", 12)
    )
    search_entry.pack(pady=10)
    search_result_frame = Frame(search_div, bg="#121212")
    search_result_frame.pack(pady=20)
    def search_student():
        student_id = search_entry.get()
        student = search_handler.verify_login(student_id)
        if student:
            show_search_result(student, search_result_frame)
        else:
            for widget in search_result_frame.winfo_children():
                widget.destroy()
            ttk.Label(
                search_result_frame, 
                text=f"No student found with ID: {student_id}", font=("Arial", 14)
            ).pack(pady=20)
    ttk.Button(
        search_form_frame, 
        text="Search", style="TButton", command=search_student
    ).pack(pady=20)
def create_student_list():
    for widget in studentList_div.winfo_children():
        widget.destroy()
    ttk.Label(
        studentList_div, text="Student List", font=("Arial", 20, "bold")
    ).pack(pady=(20, 10))
    student_list_frame = Frame(studentList_div, bg="#121212")
    student_list_frame.pack(expand=True, padx=20, pady=10)
    headers = ["Name", "Age", "Student ID", "Email", "Phone"]
    for col, header in enumerate(headers):
        ttk.Label(
            student_list_frame, 
            text=header, font=("Arial", 12, "bold")
        ).grid(row=0, column=col, padx=5, pady=5)
    student_info.read_file()
    for row, student in enumerate(student_info.all_students, start=1):
        for col, value in enumerate(student[:5]):
            ttk.Label(
                student_list_frame, text=value, font=("Arial", 11)
            ).grid(row=row, column=col, padx=5, pady=5)

def create_register_form():
    form_frame = Frame(register_div, bg="#121212")
    form_frame.pack(expand=True, padx=50, pady=20)
    ttk.Label(
        form_frame, 
        text="Register New Student", font=("Arial", 20, "bold")
    ).pack(pady=20)
    fields = [
        ("Name:", "name"),
        ("Age:", "age"),
        ("Student ID:", "student_id"),
        ("Email Address:", "email"),
        ("Phone Number:", "phone")
    ] 
    entries = {}
    for field, key in fields:
        row_frame = Frame(form_frame, bg="#121212")
        row_frame.pack(fill='x', pady=5)
        ttk.Label(
            row_frame, 
            text=field, width=20, anchor='e', font=("Arial", 14)
        ).pack(side=LEFT, padx=10)
        entries[key] = ttk.Entry(
            row_frame, 
            width=30, font=("Arial", 12)
        )
        entries[key].pack(side=LEFT)
    register_status_label = ttk.Label(
        form_frame, 
        text="", font=("Arial", 12)
    )
    register_status_label.pack(pady=10)
    def reg_stud():
        if not all(entries[key].get().strip() for key in entries):
            register_status_label.config(text="Please fill in all fields!", foreground="#CF6679")
            return
        try:
            add_student_handler.add_student(
                entries['name'].get(), 
                entries['age'].get(), 
                entries['student_id'].get(), 
                entries['email'].get(), 
                entries['phone'].get()
            )
            register_status_label.config(text=f"Student registered successfully!", foreground="#03DAC6")
            for entry in entries.values():
                entry.delete(0, END)
            create_student_list()
        except Exception as e:
            register_status_label.config(text=f"Error: {str(e)}", foreground="#CF6679")
    ttk.Button(
        form_frame, 
        text="Register", style="TButton", command=reg_stud
    ).pack(pady=20)

create_login_screen(), create_main_menu(), create_search_section(), create_register_form(), create_student_list()
login_div.pack(side="left", fill="both", expand=True)
win.geometry(f"1280x800+{(win.winfo_screenwidth()-1280)//2}+{(win.winfo_screenheight()-800)//2}")
win.mainloop()