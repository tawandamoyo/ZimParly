from pydantic import BaseModel
import datetime
from backend.app.models.processing_log import LogLevel

class ProcessingLogBase(BaseModel):
    session_id: int
    level: LogLevel
    message: str
    
class ProcessingLogCreate(ProcessingLogBase):
    pass

class ProcessingLogRead(ProcessingLogBase):
    id: int
    timestamp: datetime.datetime
    
    class Config:
        from_attributes = True