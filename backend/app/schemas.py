import uuid
import datetime
from pydantic import BaseModel, Field
from typing import List, Optional
from .models.student import RiskLevel
from .models.user import UserRole

# --- Base Schemas ---
class TunedModel(BaseModel):
    class Config:
        orm_mode = True

# --- Subject Schemas ---
class SubjectBase(TunedModel):
    name: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: uuid.UUID

# --- Evaluation Schemas ---
class EvaluationBase(TunedModel):
    score: int = Field(..., gt=0, lt=13)
    subject_id: uuid.UUID
    student_id: uuid.UUID

class EvaluationCreate(EvaluationBase):
    pass

class Evaluation(EvaluationBase):
    id: uuid.UUID
    date: datetime.datetime
    subject: Subject

# --- Student Schemas ---
class StudentBase(TunedModel):
    first_name: str
    last_name: str
    school: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: uuid.UUID
    risk_level: RiskLevel
    evaluations: List[Evaluation] = []

# --- Conversation Schemas ---
class Message(BaseModel):
    role: str
    content: str

class ConversationBase(TunedModel):
    tutor_type: str
    messages: List[Message]
    student_id: uuid.UUID

class ConversationCreate(ConversationBase):
    pass

class Conversation(ConversationBase):
    id: uuid.UUID
    start_time: datetime.datetime
    end_time: Optional[datetime.datetime]

# --- Alert Schemas ---
class AlertBase(TunedModel):
    message: str
    student_id: uuid.UUID

class AlertCreate(AlertBase):
    pass

class Alert(AlertBase):
    id: uuid.UUID
    created_at: datetime.datetime
    is_read: bool

# --- User Schemas ---
class UserBase(TunedModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: uuid.UUID
    is_active: bool
    role: UserRole

# --- Token Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
