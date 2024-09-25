from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

# Association table for many-to-many relationship
student_lesson = Table(
    'student_lesson', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('lesson_id', Integer, ForeignKey('lessons.id')),extend_existing=True,
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)

    # Relationship definitions
    lessons = relationship('Lesson', secondary=student_lesson, back_populates='students')

    def all_classes(self):
        """Return all lessons the student is enrolled in."""
        return self.lessons

    def all_lecturers(self):
        """Return all lecturers for the lessons the student is enrolled in."""
        return [lesson.lecturer for lesson in self.lessons if hasattr(lesson, 'lecturer')]

    def __repr__(self):
        return f'<Student(id={self.id}, name={self.name}, unit={self.unit})>'
