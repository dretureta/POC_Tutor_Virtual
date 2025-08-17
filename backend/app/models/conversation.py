import uuid
import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ..database import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tutor_type = Column(String) # e.g., 'math', 'language'
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    messages = Column(JSON) # Store chat history [{role: 'user'/'assistant', content: '...'}, ...]

    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"))
    student = relationship("Student", back_populates="conversations")
