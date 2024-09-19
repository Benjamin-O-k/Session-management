from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///classes.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Lecturer(Base):
    __tablename__ = 'lecturers'

    # define the attributes
    id = Column(Integer, primary_key=True)
    name = Column(String)
    profession = Column(String)

    # defining the relationship between lessons and lecturer
    lessons = relationship('Lesson', back_populates='lecturer')

    # list all lessons the lecture has been to
    def all_classes(self):
        return self.lessons()

    # list all students who have attended class
    def all_students(self):
        return [lesson.student for lesson in self.lessons]

    def __repr__(self):
        return f'<Lecturer(id={self.id}, name={self.name}, profession={self.profession})>'
