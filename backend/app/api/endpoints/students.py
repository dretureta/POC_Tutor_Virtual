from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ... import crud, models, schemas
from ...database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.student.get_students(db, skip=skip, limit=limit)
    return students

@router.post("/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.student.create_student(db=db, student=student)

@router.get("/{student_id}", response_model=schemas.Student)
def read_student(student_id: uuid.UUID, db: Session = Depends(get_db)):
    db_student = crud.student.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

from ...services import risk_analysis

@router.get("/at-risk/", response_model=List[schemas.Student])
def read_at_risk_students(db: Session = Depends(get_db)):
    """
    Retrieves students identified as being at medium or high risk.
    """
    all_students = crud.student.get_students(db, limit=1000) # Get all students for analysis
    at_risk_students = risk_analysis.get_at_risk_students(all_students)
    return at_risk_students
