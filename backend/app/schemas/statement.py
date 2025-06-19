from pydantic import BaseModel, Field
import datetime
from typing import Optional, List
from .mp import MP
from app.models.statement import Statement

class StatementBase(BaseModel):
    text: str
    