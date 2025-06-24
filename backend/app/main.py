from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import system
from app.api.v1 import mps

app = FastAPI(
    title=settings.APP_NAME,
    description="API for ZimParli Watch",
    debug=settings.DEBUG,
)

app.include_router(system.router, prefix="/api/v1", tags=["System and Health"])
app.include_router(mps.router, prefix="/api/v1/mps", tags=["Members of Parliament"])
