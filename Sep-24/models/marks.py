from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base


class Marks(Base):

    __tablename__ = "marks"

    marks_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    student_id = Column(
        Integer,
        ForeignKey("student.student_id"),
        nullable=False
    )

    subject = Column(
        String(50),
        nullable=False
    )

    marks = Column(
        Numeric(5, 2),
        nullable=False
    )

    max_marks = Column(
        Numeric(5, 2),
        default=100
    )

    student = relationship(
        "Student",
        back_populates="marks"
    )

    def __repr__(self):

        return (
            f"Marks("
            f"id={self.marks_id}, "
            f"student_id={self.student_id}, "
            f"subject='{self.subject}', "
            f"marks={self.marks})"
        )