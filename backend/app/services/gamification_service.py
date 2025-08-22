from sqlalchemy.orm import Session
from loguru import logger

from .. import crud, models

def get_or_create_badge(db: Session, name: str, description: str, icon: str) -> models.Badge:
    """Gets a badge by name or creates it if it doesn't exist."""
    badge = crud.badge.get_by_name(db, name=name)
    if not badge:
        logger.info(f"Creating new badge: {name}")
        badge = crud.badge.create(db, name=name, description=description, icon=icon)
    return badge

def award_badge(db: Session, student: models.Student, badge: models.Badge):
    """Awards a badge to a student if they don't have it already."""
    has_badge = any(sb.badge_id == badge.id for sb in student.badges)
    if not has_badge:
        logger.info(f"Awarding badge '{badge.name}' to student {student.id}")
        crud.badge.associate_to_student(db, student=student, badge=badge)
    else:
        logger.info(f"Student {student.id} already has badge '{badge.name}'")


def process_evaluation_for_rewards(db: Session, evaluation: models.Evaluation):
    """
    Processes a new evaluation and awards points and badges to the student.
    """
    student = evaluation.student
    logger.info(f"Processing evaluation for student {student.id} with score {evaluation.score}")

    points_to_award = 0
    if evaluation.score == 12:
        points_to_award = 100
        perfect_score_badge = get_or_create_badge(
            db,
            name="Nota Perfecta",
            description="Otorgado por obtener una calificación de 12 en una evaluación.",
            icon="star"
        )
        award_badge(db, student=student, badge=perfect_score_badge)
    elif evaluation.score >= 9:
        points_to_award = 50
    elif evaluation.score >= 6:
        points_to_award = 10

    if points_to_award > 0:
        logger.info(f"Awarding {points_to_award} points to student {student.id}")
        student.points += points_to_award
        db.add(student)
        db.commit()
        db.refresh(student)

    return student
