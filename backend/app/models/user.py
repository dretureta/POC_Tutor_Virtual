import uuid
import enum
from sqlalchemy import Column, String, Boolean, Enum as SQLAlchemyEnum
from sqlalchemy.dialects.postgresql import UUID
from ..database import Base

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    TEACHER = "teacher"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(SQLAlchemyEnum(UserRole), nullable=False, default=UserRole.TEACHER)
