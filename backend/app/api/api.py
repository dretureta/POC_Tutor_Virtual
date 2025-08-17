from fastapi import APIRouter

from .endpoints import students, evaluations, subjects

api_router = APIRouter()
api_router.include_router(students.router, prefix="/students", tags=["students"])
api_router.include_router(evaluations.router, prefix="/evaluations", tags=["evaluations"])
api_router.include_router(subjects.router, prefix="/subjects", tags=["subjects"])
