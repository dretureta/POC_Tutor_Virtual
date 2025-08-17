from typing import List
from loguru import logger
from ..models import Student, Evaluation, RiskLevel

def analyze_student_risk(student: Student) -> RiskLevel:
    """
    Analyzes a student's risk level based on their evaluations.
    """
    if not student.evaluations:
        return RiskLevel.LOW # Or maybe MEDIUM if no data is a risk factor

    # 1. Average score check
    average_score = sum(e.score for e in student.evaluations) / len(student.evaluations)
    if average_score < 6:
        return RiskLevel.HIGH

    # 2. Trend analysis
    # Sort evaluations by date
    sorted_evaluations = sorted(student.evaluations, key=lambda e: e.date)

    # Split evaluations into two halves
    mid_point = len(sorted_evaluations) // 2
    if mid_point > 1: # Need at least 2 evaluations in each half
        first_half_avg = sum(e.score for e in sorted_evaluations[:mid_point]) / mid_point
        second_half_avg = sum(e.score for e in sorted_evaluations[mid_point:]) / (len(sorted_evaluations) - mid_point)

        # Check for a significant downward trend
        if second_half_avg < first_half_avg * 0.9: # e.g., 10% drop
            return RiskLevel.MEDIUM

    # 3. (Future) Absence check - for now, can be inferred by low number of evals
    if len(student.evaluations) < 5: # Arbitrary threshold
        return RiskLevel.MEDIUM

    return RiskLevel.LOW

def get_at_risk_students(students: List[Student]) -> List[Student]:
    """
    Filters a list of students to return only those at medium or high risk.
    """
    logger.info(f"Running risk analysis for {len(students)} students.")
    at_risk_students = []
    for student in students:
        risk_level = analyze_student_risk(student)
        if risk_level in [RiskLevel.MEDIUM, RiskLevel.HIGH]:
            # We can update the student's risk_level attribute if we want to persist it
            # student.risk_level = risk_level
            at_risk_students.append(student)

    logger.info(f"Found {len(at_risk_students)} students at risk.")
    return at_risk_students
