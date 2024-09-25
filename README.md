# Session management

## Overview


The Session Management System is a Python-based application that manages sessions for students and lecturers. The system allows for the creation of students, lecturers, and lessons.
It also enables the management of sessions, including adding, removing, and updating sessions.

## Directory Structure

The lib folder contains python files where the classes have ben defined.

1. The `cli.py` file contains the user command line where they will be able to choose form the choices given
2. `db.py` has the initialization code of the engine where the database is create
3. `helpers.py` contain helper functions where they are used to execute commands given by the user.It also includes functions that are used across the folder.
4. `lecturer.py` ,`lesson.py`, `student.py`, are the files where the tables are defined.
5. seed.py contain sample data to input to the database

 - classes.db is the database for the entire system
 - migrations folder contains the files that track changes made to the database

## Relationships

Students and lectures have a many to many relationship through the join table lesson
The lessons have a many to one relationship with the students and the lectures

## Running the system

To run the system, you need to have python installed on your computer.
Then run the command `python cli.py` or `python3 cli.py`
Here you will find the menu of the system provided

### Exception handling.

- In the event the functions upgrade and downgrade in `env.py` do not work,use the code provided in ***special.py*** to fill in the functions in the env.py file.
- Uncomment the code in special.py then replace the code in env.py with what is given in special.py to the respective functions in env.py
- After replacing the contents of env.py with the functions provided in special.py,run the command `alembic upgrade head` in your terminal so as to create the table.
- Incase of any required modification of the tables in the database, run the command `alembic downgrade head`
