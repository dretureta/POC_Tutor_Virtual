import uuid
from sqlalchemy import Column, String, Float, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ..database import Base
import enum

class RiskLevel(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Student(Base):
    __tablename__ = "students"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    school = Column(String)
    risk_level = Column(SQLAlchemyEnum(RiskLevel), default=RiskLevel.LOW)

    evaluations = relationship("Evaluation", back_populates="student")
    conversations = relationship("Conversation", back_populates="student")
