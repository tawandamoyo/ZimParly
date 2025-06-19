import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import datetime

class ProcessingLog(Base):
    __tablename__ = "processing_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc), nullable=False)
    level = Column(SQLAlchemyEnum(LogLevel), nullable=False, index=True)
    message = Column(String(255), nullable=False)
    
    session = relationship("Session", back_populates="processing_logs")
    
    def __repr__(self):
        return f"<ProcessingLog(session_id={self.session_id}, timestamp={self.timestamp}, level={self.level}, message={self.message})>"