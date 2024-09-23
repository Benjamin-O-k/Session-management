from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class Lecturer(Base):
    __tablename__ = 'lecturers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    profession = Column(String, nullable=False)

    # Relationship with lessons
    lessons = relationship('Lesson', back_populates='lecturer')

    def all_classes(self):
        """Return all lessons the lecturer teaches."""
        return self.lessons

    def all_students(self):
        """Return all students who have attended the lecturer's classes."""
        return [student for lesson in self.lessons for student in lesson.students]

    def __repr__(self):
        return f'<Lecturer(id={self.id}, name={self.name}, profession={self.profession})>'
