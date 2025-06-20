from pydantic import BaseModel
from typing import Optional, List
from app.models.session import Session
import datetime

class SessionBase(BaseModel):
    session_date: datetime.date
    volume: int
    number: int
    source_url: Optional[str] = None
    
class SessionCreate(SessionBase):
    pass

class SessionUpdate(BaseModel):
    status: Optional[ProcessingStatus] = None
    processing_started_at: Optional[datetime.datetime] = None
    processing_finished_at: Optional[datetime.datetime] = None
    statement_count: Optional[int] = None
    
class SessionRead(SessionBase):
    id: int
    status: ProcessingStatus
    statement_count: int
    created_at: datetime.datetime
    statements: List[StatementRead] = []
    
    class Config:
        from_attributes = True