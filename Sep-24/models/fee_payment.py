from sqlalchemy import (
    Column,
    Integer,
    Date,
    Numeric,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base


class FeePayment(Base):

    __tablename__ = "fee_payment"

    payment_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    student_id = Column(
        Integer,
        ForeignKey("student.student_id"),
        nullable=False
    )

    payment_date = Column(
        Date,
        nullable=False
    )

    amount = Column(
        Numeric(10, 2),
        nullable=False
    )

    payment_mode = Column(
        String(20)
    )

    student = relationship(
        "Student",
        back_populates="fee_payments"
    )

    def __repr__(self):

        return (
            f"FeePayment("
            f"id={self.payment_id}, "
            f"student_id={self.student_id}, "
            f"amount={self.amount})"
        )