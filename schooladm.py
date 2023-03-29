class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        for student in self.students:
            print(f"{student.name}, {student.age}, Grade {student.grade}")

school = School()

while True:
    print("\nWelcome to the School Administration Program!")
    print("1. Add a student")
    print("2. View all students")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter the student's name: ")
        age = input("Enter the student's age: ")
        grade = input("Enter the student's grade: ")
        student = Student(name, age, grade)
        school.add_student(student)
        print(f"{name} has been added to the system.")

    elif choice == "2":
        print("\nAll students:")
        school.view_students()

    elif choice == "3":
        print("\nThank you for using the School Administration Program!")
        break

    else:
        print("\nInvalid choice. Please try again.")
