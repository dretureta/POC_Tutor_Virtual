from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ... import crud, models, schemas
from ...database import get_db
from .. import deps

router = APIRouter()

@router.post("/", response_model=schemas.Alert)
def create_alert(
    alert: schemas.AlertCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user)
):
    return crud.alert.create_alert(db=db, alert=alert)

@router.get("/", response_model=List[schemas.Alert])
def read_alerts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user)
):
    alerts = crud.alert.get_alerts(db, skip=skip, limit=limit)
    return alerts
