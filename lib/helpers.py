from lib.db.lecturer import Lecturer
from lib.db.lesson import Lesson
from lib.db.student import Student
from debug import Base,session


# Lesson functions
def create_lesson():
    title = str(input("Please enter the title of the class:\n "))
    location = str(input("Please provide the location of the lesson:\n "))
    time =str(input("Please provide the time of the class:\n "))
    try:
        lesson = Lesson(title=title,location=location,time=time)
        session.add(lesson)
        session.commit()

        print(f"Lesson added successfully!.{lesson}")
    except Exception as e:
        print(f"Sorry an error occurred while creating the lesson: {e}")

def find_lesson_by_name():
    name = input("Enter lesson name you want to search:\n ")
    lesson = session.query(Lesson).filter_by(Student.name.like(str(name)))
    if lesson:
        print(lesson)
    else:
        print(f"The lesson {name} has not been found.Please try again")

def all_lessons():
    lessons = session.query(Lesson).all()
    for lesson in lessons:
        print(lesson)

def students_present():
    students = Lesson.all_students
    for student in students:
        print(student)

def find_lesson_by_id():
    id_ = int(input("Enter lesson ID: \n"))
    lesson = session.query(Lesson).filter_by(Student.id.like(id_))
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
            session.query(Lesson).filter_by(Lesson.id == id_).update({
                Lesson.title: title,
                Lesson.location: location,
                Lesson.time: time,
            })
            print("Lesson updated successfully.")
        except Exception as ion:
            print("Error occurred while updating the lesson." ,ion)
    else:
        print(f"The lesson with ID {id} has not been found. Please try again")

def delete_lesson():
    id_ = int(input("Enter lesson ID to delete: \n"))

    query = session.query(Lesson).filter_by(Lesson.id == id_)
    if query:
        try:
            first_lesson = query.first()
            session.delete(first_lesson)
            session.commit()
            print("Lesson deleted successfully.")
        except Exception as e:
            print("Error occurred while deleting the lesson." ,e)
    else:
        print(f"The lesson with ID {id} has not been found. Please try again")


# Student functions

def create_student():
    name = str(input("Please enter the name of the student: "))
    unit = str(input("Please provide the unit the student will be taking: "))
    try:
        student = Student(name=name,unit=unit)
        session.add(student)
        session.commit()
        print(f"Lesson added successfully.{student}")
    except Exception as e:
        print(f"Error occurred while adding the student: {e}")

def find_student_by_name():
    name = input("Enter student name: ")
    student = session.query(Student).filter_by(Student.name.like(name))
    if student:
        print(student)
    else:
        print(f"The student named {name} has not been found.Please try again")

def find_student_by_id():
    id_ = int(input("Enter student ID: "))
    student = session.query(Student).filter_by(Student.id.like(id_))
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
            session.query(Student).filter_by(Student.id == id_).update({
                Student.name: name,
                Student.unit: unit,
            })
            print("Student updated successfully.")
        except Exception as ion:
            print("Error occurred while updating the student." ,ion)
    else:
        print(f"The student with ID {id} has not been found. Please check the students ids and try again")

def delete_student():
    id_ = int(input("Enter student ID to delete: "))

    query = session.query(Student).filter_by(Student.id == id_)
    if query:
        try:
            first_student = query.first()
            session.delete(first_student)
            session.commit()
            print("Student deleted successfully.")
        except Exception as e:
            print("Error occurred while deleting the student.Please try again later or contact the admin." ,e)
    else:
        print(f"The student with ID {id} has not been found. Please check the list of students and try again")

def stud_lecturer():
    print("All students and their lecturers")
    students = Student.all_lecturers()
    for student in students:
        print(f"{student.name}: {student.lecturer}")

def stud_class():
    print("All students and their lessons:")
    students = Student.all_classes()
    for student in students:
        print(f"{student.name}: {student.lesson}")

# lecturer functions

def create_lecturer():
    name = str(input("Enter the name: "))
    profession = str(input("Enter the profession: "))
    try:
        lecturer = Lecturer(name=name,profession=profession)
        session.add(lecturer)
        session.commit()
        print(f"Lecturer added successfully.{lecturer}")
    except Exception as e:
        print(f"Error occurred while creating the lecturer: {e}")

def find_lecturer_by_name():
    name = input("Enter lecturer name: ")
    lecturer = session.query(Lecturer).filter_by(Student.name.like(name))
    if lecturer:
        print(lecturer)
    else:
        print(f"The lecturer {name} has not been found.Please check the list of the lecturers and try again")

def find_lecturer_by_id():
    id_ = int(input("Enter lecturer ID: "))
    lecturer = session.query(Lecturer).filter_by(Student.id.like(id_))
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
            session.query(Lecturer).filter_by(Lecturer.id == id_).update({
                Lecturer.name: name,
                Lecturer.profession: profession,
            })
            print("Lecturer has been updated successfully.")
        except Exception as ion:
            print("Error occurred while updating the lecturers information." ,ion)
    else:
        print(f"The lecturer with ID {id} has not been found. Please check from the list of available lecturers and try again")

def delete_lecturer():
    id_ = int(input("Enter lecturer ID to delete: "))

    query = session.query(Lecturer).filter_by(Lecturer.id == id_)
    if query:
        try:
            first_lecturer = query.first()
            session.delete(first_lecturer)
            session.commit()
            print("Lecturer deleted successfully.")
        except Exception as e:
            print("Error occurred while deleting the lecturer." ,e)
    else:
        print(f"The lecturer with ID {id} has not been found. Please check and try again")

def lec_classes():
    print("All lecturers and their classes:")
    lecturers = Lecturer.all_classes()
    for lecturer in lecturers:
        print(f"{lecturer.name}: {lecturer.lesson}")

def lec_students():
    print("All lecturers and their students:")
    lecturers = Lecturer.all_students()
    for lecturer in lecturers:
        print(f"{lecturer.name}: {lecturer.students}")


# Main menu
def menu():
    while True:
        print("\nChoose an option:")
        print("1. Create a lesson")
        print("2. Find a lesson by name")
        print("3. List all lessons")
        print("4. List all students present in a lesson")
        print("5. Find a lesson by the id")
        print("6. Update a lesson")
        print("7. Delete a lesson")
        print("8. Create a student")
        print("9. Find a student by name")
        print("10. Find a student by id")
        print("11. Update a student")
        print("12. Delete a student")
        print("13. List all students and there lecturer")
        print("14. List all students and there lessons")
        print("15. Create a lecturer")
        print("16. Find a lecturer by the name")
        print("17. Find a lecturer by id")
        print("18. Update a lecturer information")
        print("19. Delete a lecturer's information")
        print("20. List all lecturers and their classes")
        print("21. List all lecturers and their students")
        print("23. Exit")

        choice = str(input("Enter your choice: "))

        if choice == '1':
            create_lesson()
        elif choice == '2':
            find_lesson_by_name()
        elif choice == '3':
            all_lessons()
        elif choice == '4':
            students_present()
        elif choice == '5':
            find_lesson_by_id()
        elif choice =='6':
            update_lesson()
        elif choice == '7':
            delete_lesson()
        elif choice == '8':
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
            stud_lecturer()
        elif choice == '14':
            stud_class()
        elif choice == '15':
            create_lecturer()
        elif choice == '16':
            find_lecturer_by_name()
        elif choice == '17':
            find_lecturer_by_id()
        elif choice == '18':
            update_lecturer()
        elif choice == '19':
            delete_lecturer()
        elif choice == '20':
            lec_classes()
        elif choice == '21':
            lec_students()
        elif choice == '23':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def exit_program():
    x = input("Are you sure you want to exit the program:(y/n)")
    if x.lower() == 'y':
        print("Exiting the program...")
        exit()
    else:
        print("Program will continue...")
        menu()
