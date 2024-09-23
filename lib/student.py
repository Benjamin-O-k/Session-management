from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    lesson_id = Column(Integer, ForeignKey('lessons.id'))

    # Relationship definitions
    lessons = relationship('Lesson', back_populates='students', foreign_keys=[lesson_id])

    def all_classes(self):
        """Return all lessons the student is enrolled in."""
        return self.lessons

    def all_lecturers(self):
        """Return all lecturers for the lessons the student is enrolled in."""
        return [lesson.lecturer for lesson in self.lessons]

    def __repr__(self):
        return f'<Student(id={self.id}, name={self.name}, unit={self.unit})>'
