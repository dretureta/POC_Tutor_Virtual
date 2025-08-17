from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="POC Tutor Virtual Ceibal API",
    description="API for the POC Tutor Virtual Ceibal project.",
    version="0.1.0"
)

# CORS (Cross-Origin Resource Sharing)
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5678",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .api.api import api_router

@app.get("/health", tags=["Health Check"])
def read_root():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api")
