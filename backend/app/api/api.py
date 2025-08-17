from fastapi import APIRouter

from .endpoints import students, evaluations, subjects, alerts, conversations

api_router = APIRouter()
api_router.include_router(students.router, prefix="/students", tags=["students"])
api_router.include_router(evaluations.router, prefix="/evaluations", tags=["evaluations"])
api_router.include_router(subjects.router, prefix="/subjects", tags=["subjects"])
api_router.include_router(alerts.router, prefix="/alerts", tags=["alerts"])
api_router.include_router(conversations.router, prefix="/conversations", tags=["conversations"])
