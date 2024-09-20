from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.debug import Base


class Lesson(Base):
    __tablename__ = 'lessons'

    # creating the attributes(columns)
    id = Column(Integer, primary_key=True)
    title = Column(String)
    location = Column(String)
    time = Column(String)

    # foreign keys for the lecturer and student table
    lec_id = Column(Integer, ForeignKey('lecturers.id'))
    student_id = Column(Integer, ForeignKey('students.id'))

    # relationships between lecturers and students with lessons
    students = relationship('Student', back_populates='lessons')
    lecturers = relationship('Lecturer', back_populates='lessons')

    # list all students that were at the lesson
    def all_students(self):
        return self.student

    # list all lecturers that were at the lesson
    def all_lecturers(self):
        return self.lecturer

    # gives details about the lesson
    def lesson_details(self):
        return f'Lesson ID: {self.id}, Title: {self.title}, Location: {self.location}, Lecturer: {self.lecturer.name}'

    def __repr__(self):
        return f'<Lesson(id={self.id}, title={self.title},location={self.location},lecturer={self.lecturer})>'
