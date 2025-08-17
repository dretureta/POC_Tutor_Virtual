from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import uuid

def test_create_conversation(client: TestClient, db: Session):
    student_response = client.post(
        "/api/students/",
        json={"first_name": "Conversador", "last_name": "Inicial", "school": "Liceo Dialogo"},
    )
    student_id = student_response.json()["id"]

    conversation_response = client.post(
        "/api/conversations/",
        json={
            "tutor_type": "math",
            "student_id": student_id,
            "messages": [{"role": "user", "content": "Hola, ¿puedes ayudarme?"}]
        },
    )
    assert conversation_response.status_code == 200, conversation_response.text
    data = conversation_response.json()
    assert data["tutor_type"] == "math"
    assert data["student_id"] == student_id
    assert len(data["messages"]) == 1
    assert data["messages"][0]["content"] == "Hola, ¿puedes ayudarme?"

def test_get_student_conversations(client: TestClient, db: Session):
    student_response = client.post(
        "/api/students/",
        json={"first_name": "Historial", "last_name": "DeConversa", "school": "Liceo Archivo"},
    )
    student_id = student_response.json()["id"]

    client.post(
        "/api/conversations/",
        json={
            "tutor_type": "language",
            "student_id": student_id,
            "messages": [{"role": "user", "content": "Primera conversación."}]
        },
    )

    response = client.get(f"/api/conversations/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["tutor_type"] == "language"

def test_update_conversation(client: TestClient, db: Session):
    student_response = client.post(
        "/api/students/",
        json={"first_name": "Actualizador", "last_name": "DeMensajes", "school": "Liceo Modificar"},
    )
    student_id = student_response.json()["id"]
    conversation_response = client.post(
        "/api/conversations/",
        json={
            "tutor_type": "math",
            "student_id": student_id,
            "messages": [{"role": "user", "content": "Mensaje original."}]
        },
    )
    conversation_id = conversation_response.json()["id"]

    updated_messages = [
        {"role": "user", "content": "Mensaje original."},
        {"role": "assistant", "content": "Respuesta del asistente."}
    ]

    response = client.put(
        f"/api/conversations/{conversation_id}",
        json=updated_messages,
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["messages"]) == 2
    assert data["messages"][1]["content"] == "Respuesta del asistente."
