from fastapi import APIRouter

from .endpoints import students, evaluations, subjects, alerts, conversations, auth, chat

api_router = APIRouter()

# Authentication router
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

# WebSocket router
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])

# Other routers
api_router.include_router(students.router, prefix="/students", tags=["students"])
api_router.include_router(evaluations.router, prefix="/evaluations", tags=["evaluations"])
api_router.include_router(subjects.router, prefix="/subjects", tags=["subjects"])
api_router.include_router(alerts.router, prefix="/alerts", tags=["alerts"])
api_router.include_router(conversations.router, prefix="/conversations", tags=["conversations"])
