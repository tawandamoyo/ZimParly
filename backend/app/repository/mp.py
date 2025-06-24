from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.mp import MP

def get_mp(db: Session, mp_id: int) -> Optional[MP]:
    """Retrieve a Member of Parliament by ID."""
    return db.query(MP).filter(MP.id == mp_id).first()

def get_mps(db: Session, skip: int = 0, limit: int = 100) -> List[MP]:
    """Retrieve a list of Members of Parliament with pagination."""
    return db.query(MP).offset(skip).limit(limit).all()

