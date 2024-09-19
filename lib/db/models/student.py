from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///classes.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    # define the attributes
    id = Column(Integer, primary_key=True)
    name = Column(String)
    unit = Column(String)

    # defining the relationship between lessons and students
    lessons = relationship('Lesson', back_populates='student')

    # list lessons the student attended
    def all_classes(self):
        return self.lessons()

    # list all lecturers that have been to students class
    def all_lecturers(self):
        return [lesson.lecturer for lesson in self.lessons]

    def __repr__(self):
        return f'<Student(id={self.id}, name={self.name}, unit={self.unit})>'
