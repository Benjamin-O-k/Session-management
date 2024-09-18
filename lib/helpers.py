from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db.models.lecturer import Lecturer
from db.models.lesson import Lesson
from db.models.student import Student



# Define the database engine
engine = create_engine('sqlite:///class.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# Lesson functions
def add_lesson(title, location, time):
    new_lesson = Lesson(title=title, location=location, time=time)
    session.add(new_lesson)
    session.commit()

def create_lesson():
    title = str(input("Please enter the title of the class:\n "))
    location = str(input("Please provide the location of the lesson:\n "))
    time =str(input("Please provide the time of the class:\n "))
    try:
        lesson = Lesson.create(title,location,time)
        print(f"Lesson added successfully!.{lesson}")
    except Exception as e:
        print(f"Sorry an error occurred while creating the lesson: {e}")

def find_lesson_by_name():
    name = input("Enter lesson name you want to search:\n ")
    lesson = Lesson.get_by_name(str(name))
    if lesson:
        print(lesson)
    else:
        print(f"The lesson {name} has not been found.Please try again")

def all_lessons():
    lessons = Lesson.get_all()
    for lesson in lessons:
        print(lesson)

def students_present():
    students = Lesson.all_students
    for student in students:
        print(student)

def find_lesson_by_id():
    id_ = int(input("Enter lesson ID: \n"))
    lesson = Lesson.get_by_id(id_)
    if lesson:
        print(lesson)
    else:
        print(f"The lesson with ID {id} has not been found. Please try again")

def update_lesson():
    id_ = int(input("Enter lesson ID to update: \n"))

    if lesson := Lesson.get_by_id(id_):
        try:
            title = str(input("Enter new title: \n"))
            location = str(input("Enter new location: \n"))
            time = str(input("Enter new time: \n"))
            lesson.title = title
            lesson.location = location
            lesson.time = time
            lesson.update()
            print("Lesson updated successfully.")
        except Exception as ion:
            print("Error occurred while updating the lesson." ,ion)
    else:
        print(f"The lesson with ID {id} has not been found. Please try again")

def delete_lesson():
    id_ = int(input("Enter lesson ID to delete: \n"))

    if lesson := Lesson.get_by_id(id_):
        try:
            lesson.delete()
            print("Lesson deleted successfully.")
        except Exception as e:
            print("Error occurred while deleting the lesson." ,e)
    else:
        print(f"The lesson with ID {id} has not been found. Please try again")


# Student functions
def add_student(name,unit):
    new_student = Student(name=name , unit=unit)
    session.add(new_student)
    session.commit()

def create_student():
    name = str(input("Please enter the name of the student: "))
    unit = str(input("Please provide the unit the student will be taking: "))
    try:
        student = Student.create(name,unit)
        print(f"Lesson added successfully.{student}")
    except Exception as e:
        print(f"Error occurred while adding the student: {e}")

def find_student_by_name():
    name = input("Enter student name: ")
    student = Student.get_by_name(str(name))
    if student:
        print(student)
    else:
        print(f"The student named {name} has not been found.Please try again")

def find_student_by_id():
    id_ = int(input("Enter student ID: "))
    student = Student.get_by_id(id_)
    if student:
        print(student)
    else:
        print(f"The student with ID {id} does not exist!")

def update_student():
    id_ = int(input("Enter student ID to update: "))

    if student := Student.find_by_id(id_):
        try:
            name = str(input("Enter new name: "))
            unit = str(input("Enter new unit: "))
            student.name = name
            student.unit = unit
            student.update()
            print("Student updated successfully.")
        except Exception as ion:
            print("Error occurred while updating the student." ,ion)
    else:
        print(f"The student with ID {id} has not been found. Please check the students ids and try again")

def delete_student():
    id_ = int(input("Enter student ID to delete: "))

    if student := Student.find_by_id(id_):
        try:
            student.delete()
            print("Student deleted successfully.")
        except Exception as e:
            print("Error occurred while deleting the student.Please try again later or contact the admin." ,e)
    else:
        print(f"The student with ID {id} has not been found. Please check the list of students and try again")


# lecturer functions
def add_lecturer(name,profession):
    new_lecturer = Lecturer(name=name , profession =profession)
    session.add(new_lecturer)
    session.commit()

def create_lecturer():
    name = str(input("Enter the name: "))
    profession = str(input("Enter the profession: "))
    try:
        lecturer = Lecturer.create(name,profession)
        print(f"Lecturer added successfully.{lecturer}")
    except Exception as e:
        print(f"Error occurred while creating the lecturer: {e}")

def find_lecturer_by_name():
    name = input("Enter lecturer name: ")
    lecturer = Lecturer.get_by_name(str(name))
    if lecturer:
        print(lecturer)
    else:
        print(f"The lecturer {name} has not been found.Please check the list of the lecturers and try again")

def find_lecturer_by_id():
    id_ = int(input("Enter lecturer ID: "))
    lecturer = Lecturer.get_by_id(id_)
    if lecturer:
        print(lecturer)
    else:
        print(f"The lecturer with ID {id} has not been found. Please check the list of available lecturers and try again")

def update_lecturer():
    id_ = int(input("Enter lecturer ID to update: "))

    if lecturer := Lecturer.find_by_id(id_):
        try:
            name = str(input("Enter new name: "))
            profession = str(input("Enter new profession: "))
            lecturer.name = name
            lecturer.profession = profession
            lecturer.update()
            print("Lecturer has been updated successfully.")
        except Exception as ion:
            print("Error occurred while updating the lecturers information." ,ion)
    else:
        print(f"The lecturer with ID {id} has not been found. Please check from the list of available lecturers and try again")

def delete_lecturer():
    id_ = int(input("Enter lecturer ID to delete: "))

    if lecturer := Lecturer.find_by_id(id_):
        try:
            lecturer.delete()
            print("Lecturer deleted successfully.")
        except Exception as e:
            print("Error occurred while deleting the lecturer." ,e)
    else:
        print(f"The lecturer with ID {id} has not been found. Please check and try again")













def exit_program():
    print("Exiting the program......\nGoodbye!")
    exit()
