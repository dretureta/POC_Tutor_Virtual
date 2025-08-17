from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ... import crud, schemas
from ...database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Alert)
def create_alert(alert: schemas.AlertCreate, db: Session = Depends(get_db)):
    return crud.alert.create_alert(db=db, alert=alert)

@router.get("/", response_model=List[schemas.Alert])
def read_alerts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    alerts = crud.alert.get_alerts(db, skip=skip, limit=limit)
    return alerts
