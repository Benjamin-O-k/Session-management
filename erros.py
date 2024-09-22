def students_present():
    lessons = session.query(Lesson).all()
    for lesson in lessons:
        students = lesson.students  # assuming Lesson class has a students attribute
        for student in students:
            print(student)

def stud_lecturer():
    print("All students and their lecturers")
    students = session.query(Student).all()
    for student in students:
        print(f"{student.name}: {student.lecturer}")

def stud_class():
    print("All students and their lessons:")
    students = session.query(Student).all()
    for student in students:
        print(f"{student.name}: {student.lesson}")

def stud_class():#many to one relationship between students and lessons
    print("All students and their lessons:")
    students = session.query(Student).join(Lesson).all()
    for student in students:
        print(f"{student.name}: {student.lesson.name}")


# might be correct
def stud_class():
    print("All students and their lessons:")
    students = session.query(Student).all()
    for student in students:
        print(f"{student.name}:")
        for lesson in student.lessons:
            print(f"  - {lesson.name}")
