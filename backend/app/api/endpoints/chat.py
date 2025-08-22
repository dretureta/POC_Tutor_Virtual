import httpx
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from loguru import logger
import uuid

from ... import models
from .. import deps

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections[client_id] = websocket
        logger.info(f"New WebSocket connection: {client_id}")

    def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            del self.active_connections[client_id]
        logger.info(f"WebSocket connection closed: {client_id}")

    async def send_personal_message(self, message: str, client_id: str):
        if client_id in self.active_connections:
            await self.active_connections[client_id].send_text(message)

manager = ConnectionManager()

# This is a simplified bridge. A more robust solution might use a message queue.
async def call_n8n_webhook(student_id: str, tutor_type: str, message: str) -> str:
    """Calls the appropriate n8n webhook and returns the response."""
    # The n8n service is on a different port, but accessible via its service name
    n8n_base_url = "http://n8n:5678/webhook"

    webhook_path_map = {
        "Matemáticas": "/tutor-math",
        "Lengua": "/tutor-language"
    }
    webhook_path = webhook_path_map.get(tutor_type)
    if not webhook_path:
        return "Error: Tutor no válido."

    url = f"{n8n_base_url}{webhook_path}"
    payload = {"student_id": student_id, "message": message}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, timeout=60.0)
            response.raise_for_status()
            return response.text
    except httpx.HTTPStatusError as e:
        logger.error(f"Error calling n8n webhook: {e.response.status_code} - {e.response.text}")
        return f"Lo siento, el tutor ha encontrado un error: {e.response.status_code}"
    except httpx.RequestError as e:
        logger.error(f"Error connecting to n8n: {e}")
        return "Lo siento, no puedo conectar con el servicio de tutores en este momento."


@router.websocket("/ws/chat/{student_id}/{tutor_type}")
async def websocket_endpoint(
    websocket: WebSocket,
    student_id: uuid.UUID,
    tutor_type: str,
    # Although we don't use the user object here, including it protects the endpoint
    current_user: models.User = Depends(deps.get_current_user)
):
    client_id = f"{student_id}:{tutor_type}"
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            # The user sends a message, we bridge it to n8n
            await manager.send_personal_message(f"Tutor está pensando...", client_id)

            tutor_response = await call_n8n_webhook(str(student_id), tutor_type, data)

            # Send the n8n response back to the user
            await manager.send_personal_message(tutor_response, client_id)

    except WebSocketDisconnect:
        manager.disconnect(client_id)
    except Exception as e:
        logger.error(f"An unexpected error occurred in the websocket: {e}")
        await manager.send_personal_message("Ha ocurrido un error inesperado. Por favor, reconecta.", client_id)
        manager.disconnect(client_id)
