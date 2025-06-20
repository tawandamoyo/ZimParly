from pydantic import BaseModel, Field
import datetime
from typing import Optional
from .mp import MP  # Assuming mp schema exists
from app.models.statement import ContentType

class StatementBase(BaseModel):
    text: str
    content_type: ContentType = ContentType.SPEECH
    speaker_raw: Optional[str] = None
    sequence_number: int
    page_number: Optional[int] = None
    session_id: int
    mp_id: Optional[int] = None

class StatementCreate(StatementBase):
    pass

class StatementUpdate(BaseModel):
    mp_id: Optional[int] = None
    is_processed: Optional[bool] = True
    needs_review: Optional[bool] = False
    search_vector: Optional[str] = None 

class StatementRead(StatementBase):
    id: int
    created_at: datetime.datetime
    is_processed: bool
    needs_review: bool
    mp: Optional[MP] = None

    class Config:
        from_attributes = True