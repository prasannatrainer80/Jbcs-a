from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Student(Base):

    __tablename__ = "student"

    student_id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(50),
        nullable=False
    )

    gender = Column(
        String(10)
    )

    course = Column(
        String(50)
    )

    email = Column(
        String(100)
    )

    phone = Column(
        String(15)
    )

    # Relationships

    attendance = relationship(
        "Attendance",
        back_populates="student"
    )

    marks = relationship(
        "Marks",
        back_populates="student"
    )

    fee_payments = relationship(
        "FeePayment",
        back_populates="student"
    )

    def __repr__(self):

        return (
            f"Student("
            f"id={self.student_id}, "
            f"name='{self.name}', "
            f"course='{self.course}')"
        )