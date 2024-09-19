from lib.db.models.student import Student
from lib.db.models.lecturer import Lecturer
from lib.db.models.lesson import Lesson
from faker import Faker
from helpers import session

fake = Faker()

new_lecturer1 = Lecturer(name=f"{fake.name()}", profession="Computer Science")
session.add(new_lecturer1)
session.commit()

new_lecturer2 = Lecturer(name=f"{fake.name()}", profession="Construction Management")
session.add(new_lecturer2)
session.commit()

new_lecturer3 = Lecturer(name=f"{fake.name()}", profession="Medicine")
session.add(new_lecturer3)
session.commit()


new_student1 = Student(name=f"{fake.name()}", unit="Vector Analysis")
session.add(new_student1)
session.commit()

new_student2 = Student(name=f"{fake.name()}", unit="Pure Mathematics")
session.add(new_student2)
session.commit()

new_student3 = Student(name=f"{fake.name()}", unit="Applied Mathematics")
session.add(new_student3)
session.commit()


new_lesson1 = Lesson(title="Bones", location="COPAS 201")
session.add(new_lesson1)
session.commit()

new_lesson2 = Lesson(title="Number Theory", location="SCC 204")
session.add(new_lesson2)
session.commit()

new_lesson3 = Lesson(title="Limits of a Function", location="HRD 101")
session.add(new_lesson3)
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
