from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..core.database import Base
import datetime
import enum

class Statement(Base):
    __tablename__= "statements"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nulable=False)
    sequence_order = Column(Integer, nullable=False)
    speaker_id = Column(Integer, ForeignKey("mps.id"),  nullable=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(timezone.utc))
    speaker = relationship("MP", back_populates="statements")
    session = relationship("Session", back_populates="statements")