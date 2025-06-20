from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..core.database import Base
import datetime
from datetime import timezone
import enum

class ContentType(str, enum.Enum):
    """Enum for types of parliamentary content"""
    SPEECH= "speech"
    INTERJECTION= "interjection"
    PROCEDURAL = "procedural"
    ANNOUNCEMENT = "announcement"
    POINT_OF_ORDER = "point_of_order"
    PRAYER = "prayer"
    INAUDIBLE = "inaudible"
    
class Statement(Base):
    __tablename__= "statements"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    text = Column(Text, nullable=False)
    sequence_order = Column(Integer, nullable=False)
    speaker_id = Column(Integer, ForeignKey("mps.id"),  nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now(timezone.utc))
    
    speaker = relationship("MP", back_populates="statements")
    session = relationship("Session", back_populates="statements")