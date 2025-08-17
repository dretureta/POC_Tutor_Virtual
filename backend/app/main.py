from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .logging_config import setup_logging

import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .logging_config import setup_logging

# Apply logging configuration
logger = setup_logging()

app = FastAPI(
    title="POC Tutor Virtual Ceibal API",
    description="API for the POC Tutor Virtual Ceibal project.",
    version="0.1.0"
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(
        f"Request: {request.method} {request.url.path} - Completed in {duration:.4f}s with status {response.status_code}"
    )
    return response

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
