from database import SessionLocal

from models.student import Student
from models.attendance import Attendance
from models.marks import Marks
from models.fee_payment import FeePayment




def get_all_students():

    session = SessionLocal()

    try:

        students = (
            session.query(Student)
            .order_by(Student.student_id)
            .all()
        )

        return students

    finally:

        session.close()


# ============================================================
# GET STUDENT BY ID
# ============================================================

def get_student(student_id):

    session = SessionLocal()

    try:

        student = (
            session.query(Student)
            .filter(
                Student.student_id == student_id
            )
            .first()
        )

        return student

    finally:

        session.close()


# ============================================================
# GET ATTENDANCE
# ============================================================

def get_attendance(student_id):

    session = SessionLocal()

    try:

        attendance = (
            session.query(Attendance)
            .filter(
                Attendance.student_id == student_id
            )
            .order_by(
                Attendance.attendance_date
            )
            .all()
        )

        return attendance

    finally:

        session.close()


# ============================================================
# GET MARKS
# ============================================================

def get_marks(student_id):

    session = SessionLocal()

    try:

        marks = (
            session.query(Marks)
            .filter(
                Marks.student_id == student_id
            )
            .all()
        )

        return marks

    finally:

        session.close()


# ============================================================
# GET FEE PAYMENTS
# ============================================================

def get_fee_payments(student_id):

    session = SessionLocal()

    try:

        payments = (
            session.query(FeePayment)
            .filter(
                FeePayment.student_id == student_id
            )
            .order_by(
                FeePayment.payment_date
            )
            .all()
        )

        return payments

    finally:

        session.close()


# ============================================================
# ATTENDANCE SUMMARY
# ============================================================

def get_attendance_summary(student_id):

    attendance = get_attendance(student_id)

    total = len(attendance)

    present = sum(
        1
        for a in attendance
        if a.status.lower() == "present"
    )

    absent = sum(
        1
        for a in attendance
        if a.status.lower() == "absent"
    )

    if total > 0:
        percentage = (present / total) * 100
    else:
        percentage = 0

    return {
        "total": total,
        "present": present,
        "absent": absent,
        "percentage": round(percentage, 2)
    }


# ============================================================
# MARKS SUMMARY
# ============================================================

def get_marks_summary(student_id):

    marks_list = get_marks(student_id)

    total_marks = sum(
        float(m.marks)
        for m in marks_list
    )

    maximum_marks = sum(
        float(m.max_marks)
        for m in marks_list
    )

    if maximum_marks > 0:

        percentage = (
            total_marks /
            maximum_marks
        ) * 100

    else:

        percentage = 0

    return {
        "subjects": len(marks_list),
        "total_marks": total_marks,
        "maximum_marks": maximum_marks,
        "percentage": round(percentage, 2)
    }


# ============================================================
# FEE SUMMARY
# ============================================================

def get_fee_summary(student_id):

    payments = get_fee_payments(student_id)

    total_paid = sum(
        float(p.amount)
        for p in payments
    )

    return {
        "payment_count": len(payments),
        "total_paid": total_paid
    }


