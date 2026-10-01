from database import db
from model.student import Student


class StudentService:

    @staticmethod
    def create_student(data):

        student = Student(
            name=data["name"],
            email=data["email"],
            course=data["course"]
        )

        db.session.add(student)
        db.session.commit()

        return student

    @staticmethod
    def get_all_students():

        return Student.query.all()

    @staticmethod
    def get_student_by_id(student_id):

        return db.session.get(Student, student_id)

    @staticmethod
    def update_student(student_id, data):

        student = db.session.get(Student, student_id)

        if student is None:
            return None

        student.name = data["name"]
        student.email = data["email"]
        student.course = data["course"]

        db.session.commit()

        return student

    @staticmethod
    def delete_student(student_id):

        student = db.session.get(Student, student_id)

        if student is None:
            return False

        db.session.delete(student)
        db.session.commit()

        return True