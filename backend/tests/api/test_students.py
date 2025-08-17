import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import uuid

from app import schemas

def test_create_student(client: TestClient, db: Session):
    response = client.post(
        "/api/students/",
        json={"first_name": "Juan", "last_name": "Perez", "school": "IAVA"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["first_name"] == "Juan"
    assert data["last_name"] == "Perez"
    assert "id" in data

def test_read_students(client: TestClient, db: Session):
    # Create a student first
    client.post(
        "/api/students/",
        json={"first_name": "Maria", "last_name": "Gomez", "school": "Liceo 5"},
    )

    response = client.get("/api/students/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["first_name"] == "Maria"

def test_read_student(client: TestClient, db: Session):
    create_response = client.post(
        "/api/students/",
        json={"first_name": "Pedro", "last_name": "Rodriguez", "school": "Liceo 7"},
    )
    student_id = create_response.json()["id"]

    response = client.get(f"/api/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == student_id
    assert data["first_name"] == "Pedro"

def test_read_student_not_found(client: TestClient, db: Session):
    random_id = uuid.uuid4()
    response = client.get(f"/api/students/{random_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}
