from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ... import crud, models, schemas
from ...database import get_db
from .. import deps

router = APIRouter()

@router.get("/{student_id}", response_model=List[schemas.Conversation])
def read_conversations(
    student_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user)
):
    conversations = crud.conversation.get_conversations_by_student(db, student_id=student_id)
    if not conversations:
        raise HTTPException(status_code=404, detail="No conversations found for this student")
    return conversations

@router.post("/", response_model=schemas.Conversation)
def create_conversation(
    conversation: schemas.ConversationCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user)
):
    return crud.conversation.create_conversation(db=db, conversation=conversation)

@router.put("/{conversation_id}")
def update_conversation_messages(
    conversation_id: uuid.UUID,
    messages: List[schemas.Message],
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user)
):
    updated_conversation = crud.conversation.update_conversation(db, conversation_id=conversation_id, messages=messages)
    if not updated_conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return updated_conversation
