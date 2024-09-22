from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Student(Base):
    __tablename__ = 'students'

    # define the attributes
    id = Column(Integer, primary_key=True)
    name = Column(String)
    unit = Column(String)
    lesson_id = Column(Integer, ForeignKey('lessons.id'))

    # defining the relationship between lessons and students
    lessons = relationship('Lesson', back_populates='students', foreign_keys = [lesson_id])

    # list lessons the student attended
    def all_classes(self):
        return self.lessons()

    # list all lecturers that have been to students class
    def all_lecturers(self):
        return [lesson.lecturer for lesson in self.lessons]

    def __repr__(self):
        return f'<Student(id={self.id}, name={self.name}, unit={self.unit})>'
