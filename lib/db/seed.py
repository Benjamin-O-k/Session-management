from ..lib.helpers import session
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.student import Student
from lecturer import Lecturer
from lesson import Lesson



new_lecturer1 = Lecturer(name="Dave", profession="Computer Science")
session.add(new_lecturer1)
session.commit()

new_lecturer2 = Lecturer(name="Boondocks", profession="Construction Management")
session.add(new_lecturer2)
session.commit()

new_lecturer3 = Lecturer(name="Reddington", profession="Medicine")
session.add(new_lecturer3)
session.commit()


new_student1 = Student(name="John", unit="Vector Analysis")
session.add(new_student1)
session.commit()

new_student2 = Student(name="Jane", unit="Pure Mathematics")
session.add(new_student2)
session.commit()

new_student3 = Student(name="Ben", unit="Applied Mathematics")
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
    print(f'Lesson: {lesson.title} ,{lesson.location}')
