from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import csv
import io
from fastapi import UploadFile, File, BackgroundTasks
from ... import crud, models, schemas
from ...database import get_db
from .. import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Student])
def read_students(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user)
):
    students = crud.student.get_students(db, skip=skip, limit=limit)
    return students

@router.post("/", response_model=schemas.Student)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user)
):
    return crud.student.create_student(db=db, student=student)

@router.get("/{student_id}", response_model=schemas.StudentProfile)
def read_student(
    student_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user)
):
    db_student = crud.student.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

from ...services import risk_analysis

def process_csv_upload(file_content: str, db: Session):
    """
    Parses CSV content and creates students in the database.
    Expected headers: first_name,last_name,school
    """
    reader = csv.DictReader(io.StringIO(file_content))
    for row in reader:
        student_in = schemas.StudentCreate(
            first_name=row.get("first_name"),
            last_name=row.get("last_name"),
            school=row.get("school")
        )
        crud.student.create_student(db, student=student_in)

@router.post("/upload-csv")
async def upload_student_csv(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_active_admin)
):
    """
    Uploads a CSV file with student data to be created in the background.
    """
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV.")

    file_content = await file.read()
    background_tasks.add_task(process_csv_upload, file_content.decode("utf-8"), db)

    return {"message": "El archivo CSV se está procesando en segundo plano. Los estudiantes aparecerán en breve."}


@router.get("/at-risk/", response_model=List[schemas.Student])
def read_at_risk_students(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user)
):
    """
    Retrieves students identified as being at medium or high risk.
    """
    all_students = crud.student.get_students(db, limit=1000) # Get all students for analysis
    at_risk_students = risk_analysis.get_at_risk_students(all_students)
    return at_risk_students
