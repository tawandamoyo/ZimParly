from pydantic import BaseModel, Field
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

clas