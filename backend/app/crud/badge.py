from sqlalchemy.orm import Session
from .. import models

def get_by_name(db: Session, name: str) -> models.Badge | None:
    return db.query(models.Badge).filter(models.Badge.name == name).first()

def create(db: Session, name: str, description: str, icon: str) -> models.Badge:
    db_badge = models.Badge(name=name, description=description, icon=icon)
    db.add(db_badge)
    db.commit()
    db.refresh(db_badge)
    return db_badge

def associate_to_student(db: Session, student: models.Student, badge: models.Badge) -> models.StudentBadge:
    association = models.StudentBadge(student_id=student.id, badge_id=badge.id)
    db.add(association)
    db.commit()
    db.refresh(association)
    return association
