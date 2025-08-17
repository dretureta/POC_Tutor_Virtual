from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ... import crud, schemas
from ...database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Evaluation)
def create_evaluation(evaluation: schemas.EvaluationCreate, db: Session = Depends(get_db)):
    return crud.evaluation.create_evaluation(db=db, evaluation=evaluation)
