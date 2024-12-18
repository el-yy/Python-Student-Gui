class StudentInfo:
    def __init__(self):
        self.name = ''
        self.age = ''
        self.id_num = ''
        self.email = ''
        self.phone = ''
        self.all_students = []  # List to store all student information
        self.read_file()

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setIDNum(self, id_num):
        self.id_num = id_num  # Fixed typo (was self.idnum)

    def setEmail(self, email):
        self.email = email

    def setPhoneNum(self, phone):
        self.phone = phone

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getIDNum(self):
        return self.id_num

    def getEmail(self):
        return self.email

    def getPhoneNum(self):
        return self.phone

    def __str__(self):
        return f'\nName: {self.name}\nAge: {self.age}\nID Number: {self.id_num}\nEmail Address: {self.email}\nPhone Number: {self.phone}\n'

    def read_file(self):
        self.all_students.clear()  # Ensure the list is cleared before adding data
        try:
            with open("student_data.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    student_info = line.strip().split(", ")
                    if len(student_info) == 5:  # Ensure we have all 5 pieces of information
                        self.all_students.append(student_info)
            print("Yey! Student Data successfully added to the list!")
        except FileNotFoundError:
            print("There is no existing student data found.")

    def refresh_data(self):
        self.read_file()  # Call read_file, which already clears and repopulates the list
