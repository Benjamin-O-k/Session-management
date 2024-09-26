from models.lecturer import Lecturer
from models.lesson import Lesson
from models.student import Student
from db import session
import sqlalchemy

# Lesson functions
def create_lesson():
    title = input("Please enter the title of the class:\n ")
    location = input("Please provide the location of the lesson:\n ")
    time = input("Please provide the time of the class:\n ")
    lec_id = int(input("Enter the lecturer ID:\n"))
    student_id = int(input("Enter student ID:\n"))

    lecturer = session.query(Lecturer).filter_by(id=lec_id).first()
    student = session.query(Student).filter_by(id=student_id).first()

    if lecturer and student:
        try:
            lesson = Lesson(title=title, location=location, time=time, lec_id=lec_id)
            lesson.students.append(student)  # Associate student with lesson
            session.add(lesson)
            session.commit()
            print(f"Lesson added successfully: {lesson}")
        except Exception as e:
            print(f"Error occurred while creating the lesson: {e}")
    else:
        print(f"Lecturer with ID {lec_id} or Student with ID {student_id} not found.")

def find_lesson_by_name():
    name = input("Enter lesson name you want to search:\n ")
    lessons = session.query(Lesson).filter(Lesson.title.like(f'%{name}%')).all()
    if lessons:
        for lesson in lessons:
            print(f"Lesson found: {lesson.title}")
    else:
        print(f"The lesson {name} has not been found. Please try again.")

def all_lessons():
    lessons = session.query(Lesson).all()
    if lessons:
        for lesson in lessons:
            print(f"Title: {lesson.title}, Location: {lesson.location}, Time: {lesson.time}")
    else:
        print("No lessons found.")

def students_present(lesson_id):
    lesson = session.query(Lesson).get(lesson_id)
    if lesson:
        students = lesson.students
        if students:
            for student in students:
                print(student)
        else:
            print("No students present in this lesson.")
    else:
        print(f"No lesson found with ID {lesson_id}.")

def find_lesson_by_id():
    id_ = int(input("Enter lesson ID: \n"))
    lesson = session.query(Lesson).get(id_)
    if lesson:
        print(f"Lesson found: Title - {lesson.title}, Location - {lesson.location}, Time - {lesson.time}")
    else:
        print(f"The lesson with ID {id_} has not been found. Please try again.")

def update_lesson():
    id_ = int(input("Enter lesson ID to update: \n"))
    lesson = session.query(Lesson).get(id_)
    if lesson:
        try:
            lesson.title = input("Enter new title: \n")
            lesson.location = input("Enter new location: \n")
            lesson.time = input("Enter new time: \n")
            session.commit()
            print("Lesson updated successfully.")
        except Exception as e:
            print("Error occurred while updating the lesson:", e)
    else:
        print(f"The lesson with ID {id_} has not been found. Please try again.")

def delete_lesson():
    id_ = int(input("Enter lesson ID to delete: \n"))
    lesson = session.query(Lesson).get(id_)
    if lesson:
        try:
            session.delete(lesson)
            session.commit()
            print("Lesson deleted successfully.")
        except Exception as e:
            print("Error occurred while deleting the lesson:", e)
    else:
        print(f"The lesson with ID {id_} has not been found. Please try again.")

# Student functions
def create_student():
    name = input("Please enter the name of the student: \n")
    unit = input("Please provide the unit the student will be taking: \n")
    try:
        student = Student(name=name, unit=unit)
        session.add(student)
        session.commit()
        print(f"Student added successfully: {student}")
    except Exception as e:
        print(f"Error occurred while adding the student: {e}")

def find_student_by_name():
    name = input("Enter student name: \n")
    student = session.query(Student).filter_by(name=name).first()
    if student:
        print(f"Student found: {student}")
    else:
        print(f"The student named {name} has not been found. Please try again.")

def find_student_by_id():
    id_ = int(input("Enter student ID:\n "))
    student = session.query(Student).get(id_)
    if student:
        print(f"Student found: {student}")
    else:
        print(f"The student with ID {id_} does not exist!")

def update_student():
    id_ = int(input("Enter student ID to update:\n "))
    student = session.query(Student).get(id_)
    if student:
        try:
            student.name = input("Enter new name:\n ")
            student.unit = input("Enter new unit:\n ")
            session.commit()
            print("Student updated successfully.")
        except Exception as e:
            print("Error occurred while updating the student:", e)
    else:
        print(f"The student with ID {id_} has not been found. Please try again.")

def delete_student():
    id_ = int(input("Enter student ID to delete:\n "))
    student = session.query(Student).get(id_)
    if student:
        try:
            session.delete(student)
            session.commit()
            print("Student deleted successfully.")
        except Exception as e:
            print("Error occurred while deleting the student:", e)
    else:
        print(f"The student with ID {id_} has not been found. Please try again.")


def stud_class():
    print("All students and their lessons:")
    students = session.query(Student).all()
    for student in students:
        print(f"{student.name}: {[lesson.title for lesson in student.lessons]}")

# Lecturer functions
def create_lecturer():
    name = input("Enter the name:\n ")
    profession = input("Enter the profession: \n")
    try:
        lecturer = Lecturer(name=name, profession=profession)
        session.add(lecturer)
        session.commit()
        print(f"Lecturer added successfully: {lecturer}")
    except sqlalchemy.exc.IntegrityError as e:
        print(f"Error: Lecturer with the same name and profession already exists. {e}")
    except sqlalchemy.exc.OperationalError as e:
        print(f"Error: Database operational error. {e}")
    except Exception as e:
        print(f"Error occurred while creating the lecturer: {e}")

def find_lecturer_by_name():
    name = input("Enter lecturer name: \n")
    try:
        lecturers = session.query(Lecturer).filter_by(name=name).all()
        if lecturers:
            for lecturer in lecturers:
                print(f"Lecturer name: {lecturer.name}, Profession: {lecturer.profession}")
        else:
            print(f"The lecturer {name} has not been found. Please try again.")
    except sqlalchemy.exc.OperationalError as e:
        print(f"Error: Database operational error. {e}")
    except Exception as e:
        print(f"Error occurred while finding the lecturer: {e}")

def find_lecturer_by_id():
    id_ = int(input("Enter lecturer ID:\n "))
    lecturer = session.query(Lecturer).filter_by(id=id_).first()
    if lecturer:
        print(f"Lecturer found: {lecturer}")
    else:
        print(f"The lecturer with ID {id_} has not been found. Please try again.")

def update_lecturer():
    id_ = int(input("Enter lecturer ID to update: \n"))
    lecturer = session.query(Lecturer).filter_by(id=id_).first()
    if lecturer:
        try:
            lecturer.name = input("Enter new name: \n")
            lecturer.profession = input("Enter new profession:\n ")
            session.commit()
            print("Lecturer updated successfully.")
        except sqlalchemy.exc.OperationalError as e:
            print(f"Error: Database operational error. {e}")
        except Exception as e:
            print(f"Error occurred while updating the lecturer's information: {e}")
    else:
        print(f"The lecturer with ID {id_} has not been found. Please try again.")

def delete_lecturer():
    id_ = int(input("Enter lecturer ID to delete:\n "))
    lecturer = session.query(Lecturer).filter_by(id=id_).first()
    if lecturer:
        try:
            session.delete(lecturer)
            session.commit()
            print("Lecturer deleted successfully.")
        except Exception as e:
            print("Error occurred while deleting the lecturer:", e)
    else:
        print(f"The lecturer with ID {id_} has not been found. Please try again.")

def lec_classes():
    print("All lecturers and their classes:")
    lecturers = session.query(Lecturer).all()
    for lecturer in lecturers:
        print(f"{lecturer.name}: {[lesson.title for lesson in lecturer.lessons]}")

# Main menu
def home():
    while True:
        print("\n")
        print("\t\t\t\t ' ********** WELCOME TO SESSION MANAGEMENT SYSTEM ********** ' \n")
        print("CHOOSE THE SYB MENU YOU WANT TO GO TO\n")
        print("1. Lessons\n")
        print("2. students\n")
        print("3. Lecturers\n")
        print("0. Exit")

        menu = int(input("Enter your choice: \n"))

        if menu == 1:
            lessons()
        elif menu == 2:
            students()
        elif menu == 3:
            lecturers()
        elif menu ==0:
            print("Exiting the program...")
            exit()
        else:
            print("Invalid choice. Please try again.")

def lessons():
    while True:
        print("\t\t\t\t******* Welcome to the lessons menu.**********\n")
        print("1. Create a lesson")
        print("2. Find a lesson by name")
        print("3. List all lessons")
        print("4. List all students present in a lesson")
        print("5. Find a lesson by ID")
        print("6. Update a lesson")
        print("7. Delete a lesson")
        print("98. Back to main menu")

        choice = input("Please select an option from the list above:\n")

        if choice == '1':
            create_lesson()
        elif choice == '2':
            find_lesson_by_name()
        elif choice == '3':
            all_lessons()
        elif choice == '4':
            lesson_id = int(input("Enter lesson ID to list students: "))
            students_present(lesson_id)
        elif choice == '5':
            find_lesson_by_id()
        elif choice == '6':
            update_lesson()
        elif choice == '7':
            delete_lesson()
        elif choice == '98':
            home()
        else:
            print("Invalid choice. Please try again.")

def students():
    while True:
        print("\t\t\t\t **********Welcome to the students menu.*********\n")
        print("8. Create a student")
        print("9. Find a student by name")
        print("10. Find a student by ID")
        print("11. Update a student")
        print("12. Delete a student")
        print("13. List all students and their lessons")
        print("98. Back to main menu")

        choice = input("Please select an option from the list above:\n")
        if choice == '8':
                create_student()
        elif choice == '9':
                find_student_by_name()
        elif choice == '10':
                find_student_by_id()
        elif choice == '11':
                update_student()
        elif choice == '12':
                delete_student()
        elif choice == '13':
                stud_class()
        elif choice == "98":
            home()
        else:
            print("Invalid choice. Please try again.")

def lecturers():
    while True:
        print("\t\t\t\t ********Welcome to the lecturer menu.********\n")
        print("14. Create a lecturer")
        print("15. Find a lecturer by name")
        print("16. Find a lecturer by ID")
        print("17. Update a lecturer")
        print("18. Delete a lecturer")
        print("19. List all lecturers and their classes")
        print("98. Back to main menu")

        choice = input("\nPlease select an option from the list above:\n")
        if choice == '14':
            create_lecturer()
        elif choice == '15':
            find_lecturer_by_name()
        elif choice == '16':
            find_lecturer_by_id()
        elif choice == '17':
            update_lecturer()
        elif choice == '18':
            delete_lecturer()
        elif choice == '19':
            lec_classes()
        elif choice =='98':
            home()
        else:
            print("Invalid choice. Please try again.")

def items():
    home()
    lessons()
    students()
    lecturers()
