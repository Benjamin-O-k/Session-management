from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    location = Column(String, nullable=False)
    time = Column(String, nullable=False)

    # Foreign key for the lecturer
    lec_id = Column(Integer, ForeignKey('lecturers.id'))
    lecturer = relationship('Lecturer', back_populates='lessons')

    # Relationship for students
    students = relationship('Student', back_populates='lessons', foreign_keys='Student.lesson_id')

    def all_students(self):
        """Return all students enrolled in the lesson."""
        return self.students

    def lesson_details(self):
        """Return details about the lesson."""
        return f'Lesson ID: {self.id}, Title: {self.title}, Location: {self.location}, Lecturer: {self.lecturer.name}'

    def __repr__(self):
        return f'<Lesson(id={self.id}, title={self.title}, location={self.location}, lecturer={self.lecturer})>'
