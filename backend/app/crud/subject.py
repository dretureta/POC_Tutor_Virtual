from sqlalchemy.orm import Session
from .. import models

def get_subject_by_name(db: Session, name: str):
    return db.query(models.Subject).filter(models.Subject.name == name).first()
