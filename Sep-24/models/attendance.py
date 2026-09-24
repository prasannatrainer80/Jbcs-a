from sqlalchemy import (
    Column,
    Integer,
    Date,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base


class Attendance(Base):

    __tablename__ = "attendance"

    attendance_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    student_id = Column(
        Integer,
        ForeignKey("student.student_id"),
        nullable=False
    )

    attendance_date = Column(
        Date,
        nullable=False
    )

    status = Column(
        String(10),
        nullable=False
    )

    student = relationship(
        "Student",
        back_populates="attendance"
    )

    def __repr__(self):

        return (
            f"Attendance("
            f"id={self.attendance_id}, "
            f"student_id={self.student_id}, "
            f"date={self.attendance_date}, "
            f"status='{self.status}')"
        )