from database import engine, Base

from models.student import Student
from models.attendance import Attendance
from models.marks import Marks
from models.fee_payment import FeePayment

from services.student_service import (
    get_all_students,
    get_student,
    get_attendance,
    get_marks,
    get_fee_payments,
    get_attendance_summary,
    get_marks_summary,
    get_fee_summary
)


# ============================================================
# CREATE TABLES IF THEY DO NOT EXIST
# ============================================================

Base.metadata.create_all(engine)

print("=" * 60)
print("       STUDENT MANAGEMENT SYSTEM")
print("=" * 60)

print("\nMySQL database connected successfully.")


# ============================================================
# DISPLAY ALL STUDENTS
# ============================================================

print("\n")
print("=" * 60)
print("ALL STUDENTS")
print("=" * 60)

students = get_all_students()

for student in students:

    print(
        f"ID: {student.student_id:<3} "
        f"Name: {student.name:<12} "
        f"Gender: {student.gender:<8} "
        f"Course: {student.course}"
    )


# ============================================================
# SELECT STUDENT
# ============================================================

student_id = int(
    input("\nEnter Student ID: ")
)


student = get_student(student_id)


if student is None:

    print("\nStudent not found.")

else:

    # --------------------------------------------------------
    # STUDENT DETAILS
    # --------------------------------------------------------

    print("\n")
    print("=" * 60)
    print("STUDENT DETAILS")
    print("=" * 60)

    print("Student ID :", student.student_id)
    print("Name       :", student.name)
    print("Gender     :", student.gender)
    print("Course     :", student.course)
    print("Email      :", student.email)
    print("Phone      :", student.phone)


    # --------------------------------------------------------
    # ATTENDANCE
    # --------------------------------------------------------

    print("\n")
    print("=" * 60)
    print("ATTENDANCE")
    print("=" * 60)

    attendance_list = get_attendance(
        student_id
    )

    for attendance in attendance_list:

        print(
            attendance.attendance_date,
            "->",
            attendance.status
        )


    # --------------------------------------------------------
    # ATTENDANCE SUMMARY
    # --------------------------------------------------------

    attendance_summary = (
        get_attendance_summary(student_id)
    )

    print("\nAttendance Summary")

    print(
        "Total Days :",
        attendance_summary["total"]
    )

    print(
        "Present    :",
        attendance_summary["present"]
    )

    print(
        "Absent     :",
        attendance_summary["absent"]
    )

    print(
        "Percentage :",
        attendance_summary["percentage"],
        "%"
    )


    # --------------------------------------------------------
    # MARKS
    # --------------------------------------------------------

    print("\n")
    print("=" * 60)
    print("MARKS")
    print("=" * 60)

    marks_list = get_marks(
        student_id
    )

    for mark in marks_list:

        print(
            f"{mark.subject:<20}"
            f"{float(mark.marks):>6.2f} / "
            f"{float(mark.max_marks):.2f}"
        )


    # --------------------------------------------------------
    # MARKS SUMMARY
    # --------------------------------------------------------

    marks_summary = (
        get_marks_summary(student_id)
    )

    print("\nMarks Summary")

    print(
        "Subjects      :",
        marks_summary["subjects"]
    )

    print(
        "Total Marks   :",
        marks_summary["total_marks"]
    )

    print(
        "Maximum Marks :",
        marks_summary["maximum_marks"]
    )

    print(
        "Percentage    :",
        marks_summary["percentage"],
        "%"
    )


    # --------------------------------------------------------
    # FEE PAYMENTS
    # --------------------------------------------------------

    print("\n")
    print("=" * 60)
    print("FEE PAYMENTS")
    print("=" * 60)

    payments = get_fee_payments(
        student_id
    )

    for payment in payments:

        print(
            payment.payment_date,
            "-> ₹",
            float(payment.amount),
            "->",
            payment.payment_mode
        )


    # --------------------------------------------------------
    # FEE SUMMARY
    # --------------------------------------------------------

    fee_summary = (
        get_fee_summary(student_id)
    )

    print("\nFee Summary")

    print(
        "Number of Payments :",
        fee_summary["payment_count"]
    )

    print(
        "Total Paid         : ₹",
        fee_summary["total_paid"]
    )


print("\n")
print("=" * 60)
print("Program completed")
print("=" * 60)