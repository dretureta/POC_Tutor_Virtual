from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

def test_create_alert(client: TestClient, db: Session):
    # First, create a student to associate the alert with
    student_response = client.post(
        "/api/students/",
        json={"first_name": "Test", "last_name": "StudentForAlert", "school": "Liceo Test"},
    )
    student_id = student_response.json()["id"]

    # Now, create the alert
    alert_response = client.post(
        "/api/alerts/",
        json={"message": "Este es un mensaje de alerta de prueba.", "student_id": student_id},
    )
    assert alert_response.status_code == 200, alert_response.text
    data = alert_response.json()
    assert data["message"] == "Este es un mensaje de alerta de prueba."
    assert data["student_id"] == student_id
    assert data["is_read"] is False

def test_read_alerts(client: TestClient, db: Session):
    # First, create a student and an alert
    student_response = client.post(
        "/api/students/",
        json={"first_name": "Otro", "last_name": "Estudiante", "school": "Liceo Prueba"},
    )
    student_id = student_response.json()["id"]
    client.post(
        "/api/alerts/",
        json={"message": "Alerta para la prueba de lectura.", "student_id": student_id},
    )

    # Read alerts
    response = client.get("/api/alerts/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["message"] == "Alerta para la prueba de lectura."
