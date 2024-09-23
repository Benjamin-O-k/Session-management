class StudentError(Exception):
    """Base class for exceptions related to student operations."""
    pass

class StudentNotFoundError(StudentError):
    """Raised when a student is not found in the database."""
    def __init__(self, student_id):
        super().__init__(f"Student with ID {student_id} not found.")

class DuplicateStudentError(StudentError):
    """Raised when trying to add a student that already exists."""
    def __init__(self, student_name):
        super().__init__(f"Student '{student_name}' already exists.")

class LessonError(Exception):
    """Base class for exceptions related to lesson operations."""
    pass

class LessonNotFoundError(LessonError):
    """Raised when a lesson is not found in the database."""
    def __init__(self, lesson_id):
        super().__init__(f"Lesson with ID {lesson_id} not found.")

class LecturerError(Exception):
    """Base class for exceptions related to lecturer operations."""
    pass

class LecturerNotFoundError(LecturerError):
    """Raised when a lecturer is not found in the database."""
    def __init__(self, lecturer_id):
        super().__init__(f"Lecturer with ID {lecturer_id} not found.")

class DatabaseError(Exception):
    """General class for database-related exceptions."""
    def __init__(self, message):
        super().__init__(f"Database error: {message}")

# Example usage within a function
def find_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        raise StudentNotFoundError(student_id)
    return student
