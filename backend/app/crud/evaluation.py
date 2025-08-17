from sqlalchemy.orm import Session
from .. import models, schemas

def create_evaluation(db: Session, evaluation: schemas.EvaluationCreate):
    db_evaluation = models.Evaluation(**evaluation.dict())
    db.add(db_evaluation)
    db.commit()
    db.refresh(db_evaluation)
    return db_evaluation
