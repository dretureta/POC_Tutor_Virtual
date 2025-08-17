from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from ... import crud, models
from ...database import get_db

router = APIRouter()

@router.get("/{subject_name}/analytics")
def get_subject_analytics(subject_name: str, db: Session = Depends(get_db)):
    subject = crud.subject.get_subject_by_name(db, name=subject_name)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    # Basic analytics
    analytics = (
        db.query(
            func.count(models.Evaluation.id).label("evaluation_count"),
            func.avg(models.Evaluation.score).label("average_score"),
        )
        .filter(models.Evaluation.subject_id == subject.id)
        .one()
    )

    return {
        "subject_id": subject.id,
        "subject_name": subject.name,
        "evaluation_count": analytics.evaluation_count,
        "average_score": round(analytics.average_score, 2) if analytics.average_score else 0,
    }
