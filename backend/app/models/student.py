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

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped

class Student(Base):
    __tablename__ = "students"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    school = Column(String)
    risk_level = Column(SQLAlchemyEnum(RiskLevel), default=RiskLevel.LOW)
    points = Column(Integer, default=0, nullable=False)

    evaluations = relationship("Evaluation", back_populates="student")
    conversations = relationship("Conversation", back_populates="student")
    # Use string for forward reference to avoid circular import
    badges: Mapped[list["StudentBadge"]] = relationship("StudentBadge", back_populates="student")
