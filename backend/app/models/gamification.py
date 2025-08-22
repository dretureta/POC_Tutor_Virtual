import uuid
import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.dialects.postgresql import UUID
from ..database import Base

class Badge(Base):
    __tablename__ = "badges"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    icon = Column(String, nullable=False) # e.g., a name or URL for an icon

class StudentBadge(Base):
    """Association object for the many-to-many relationship between Student and Badge."""
    __tablename__ = "student_badge"

    student_id: Mapped[uuid.UUID] = Column(ForeignKey("students.id"), primary_key=True)
    badge_id: Mapped[uuid.UUID] = Column(ForeignKey("badges.id"), primary_key=True)
    earned_at: Mapped[datetime.datetime] = Column(DateTime, default=datetime.datetime.utcnow)

    # Use string for forward reference to avoid circular import
    student: Mapped["Student"] = relationship(back_populates="badges")
    badge: Mapped["Badge"] = relationship()
