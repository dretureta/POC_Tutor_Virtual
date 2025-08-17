from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ... import crud, models, schemas
from ...database import get_db
from .. import deps

router = APIRouter()

@router.post("/", response_model=schemas.Evaluation)
def create_evaluation(
    evaluation: schemas.EvaluationCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user)
):
    return crud.evaluation.create_evaluation(db=db, evaluation=evaluation)
