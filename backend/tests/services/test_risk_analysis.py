import pytest
import datetime
from app.models import Student, Evaluation, RiskLevel
from app.services.risk_analysis import analyze_student_risk

# --- Mock Data ---
def create_mock_student_with_evaluations(scores, dates=None):
    student = Student(id="test-student", first_name="Test", last_name="Student", school="Test School")
    if dates is None:
        # Create dates that match the number of scores
        today = datetime.datetime.utcnow()
        dates = [today - datetime.timedelta(days=30 * i) for i in range(len(scores))]

    evaluations = []
    for i, score in enumerate(scores):
        evaluations.append(
            Evaluation(score=score, date=dates[i], student_id=student.id, subject_id="test-subject")
        )

    # The relationship is not automatically populated in tests like this, so we set it manually
    student.evaluations = evaluations
    return student

# --- Test Cases ---

def test_risk_level_high_on_low_average():
    """Test that risk is HIGH if the average score is below 6."""
    student = create_mock_student_with_evaluations([4, 5, 6, 5, 7]) # Average is 5.4
    risk = analyze_student_risk(student)
    assert risk == RiskLevel.HIGH

def test_risk_level_medium_on_downward_trend():
    """Test that risk is MEDIUM if there is a clear downward trend."""
    student = create_mock_student_with_evaluations([10, 9, 8, 7, 6, 7]) # Average > 6, but trend is down
    risk = analyze_student_risk(student)
    assert risk == RiskLevel.MEDIUM

def test_risk_level_medium_on_few_evaluations():
    """Test that risk is MEDIUM if the student has very few evaluations."""
    student = create_mock_student_with_evaluations([10, 10, 9]) # Average is high, but only 3 evals
    risk = analyze_student_risk(student)
    assert risk == RiskLevel.MEDIUM

def test_risk_level_low_for_good_student():
    """Test that risk is LOW for a student with good and stable scores."""
    student = create_mock_student_with_evaluations([8, 9, 8, 9, 10, 8, 9])
    risk = analyze_student_risk(student)
    assert risk == RiskLevel.LOW

def test_risk_level_low_with_no_evaluations():
    """Test that risk is LOW if a student has no evaluations."""
    student = Student(id="no-evals", first_name="New", last_name="Kid")
    student.evaluations = []
    risk = analyze_student_risk(student)
    assert risk == RiskLevel.LOW

def test_risk_level_not_medium_if_trend_is_up():
    """Test that risk is not medium if trend is upward."""
    student = create_mock_student_with_evaluations([6, 7, 8, 9, 10])
    risk = analyze_student_risk(student)
    assert risk == RiskLevel.LOW
