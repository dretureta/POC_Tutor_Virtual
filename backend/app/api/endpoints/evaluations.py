from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ... import crud, models, schemas
from ...database import get_db
from ...services import gamification_service
from .. import deps

router = APIRouter()

@router.post("/", response_model=schemas.Evaluation)
def create_evaluation(
    evaluation: schemas.EvaluationCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user)
):
    db_evaluation = crud.evaluation.create_evaluation(db=db, evaluation=evaluation)
    # After creating the evaluation, process it for rewards
    gamification_service.process_evaluation_for_rewards(db=db, evaluation=db_evaluation)
    return db_evaluation
