from fastapi import FastAPI
from .chore.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="API for ZimParli Watch",
    debug=settings.DEBUG,
)

@app.get("/")
def read_root():
    """
    Root endpoint of API
    """
    return {"message": "Welcome to ZimParli Watch API"}

@app.get("/health", tags=["Monitoring"])
def health_check():
    """
    Health check endpoint
    """
    return {"status": "ok", "log_level": settings.LOG_LEVEL}