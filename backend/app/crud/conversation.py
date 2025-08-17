from sqlalchemy.orm import Session
from .. import models, schemas
import uuid

def get_conversations_by_student(db: Session, student_id: uuid.UUID):
    return db.query(models.Conversation).filter(models.Conversation.student_id == student_id).all()

def create_conversation(db: Session, conversation: schemas.ConversationCreate):
    db_conversation = models.Conversation(**conversation.dict())
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation

def update_conversation(db: Session, conversation_id: uuid.UUID, messages: list):
    db_conversation = db.query(models.Conversation).filter(models.Conversation.id == conversation_id).first()
    if db_conversation:
        db_conversation.messages = messages
        db.commit()
        db.refresh(db_conversation)
    return db_conversation
