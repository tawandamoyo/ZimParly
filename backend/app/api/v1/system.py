from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/")
def read_root():
    """
    Root endpoint with welcome message
    """
    return {"message": f"Welcome to {settings.APP_NAME}"}

@router.get("/health", tags=["Monitoring"])
def health_check():
    """
    Health check endpoint to verify API status
    """
    return {"status": "ok", "log_level": settings.LOG_LEVEL}