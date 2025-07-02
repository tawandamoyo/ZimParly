from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.session import Session

def get_session(db: Session, session_id: int) -> Optional[Session]:
    """Retrieve a Session by ID."""
    return db.query(Session).filter(Session.id == session_id).first()

def get_sessions(db: Session, skip: int = 0, limit: int = 100) -> List[Session]:
    """Retrieve a list of Sessions with pagination."""
    return db.query(Session).offset(skip).limit(limit).all()
