import uuid
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ..database import Base
import datetime

class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    score = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.utcnow)

    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"))
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subjects.id"))

    student = relationship("Student", back_populates="evaluations")
    subject = relationship("Subject", back_populates="evaluations")
