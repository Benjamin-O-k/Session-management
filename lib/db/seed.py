from lib.db.models.student import Student
from lib.db.models.lecturer import Lecturer
from lib.db.models.lesson import Lesson
from faker import Faker
from helpers import session

fake = Faker()

new_lecturer = Lecturer(name=f"{fake.name()}", profession="Computer Science")
session.add(new_lecturer)
session.commit()


new_student = Student(name=f"{fake.name()}", unit="Vector Analysis")
session.add(new_student)
session.commit()


new_lesson = Lesson(title="Limits of a Function", location="HRD 101")
session.add(new_lesson)
session.commit()


students = session.query(Student).all()
lecturers = session.query(Lecturer).all()
lessons = session.query(Lesson).all()

# print each case
for student in students:
    print(f"Student :{student.name}, {student.unit}")

for lecturer in lecturers:
    print(f'Lecturer: {lecturer.name}, {lecturer.profession}')

for lesson in lessons:
    print(f'Lesson: {lesson.title} ,{lesson.loction} ,{lesson.time}')
