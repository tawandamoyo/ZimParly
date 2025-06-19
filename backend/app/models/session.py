import enum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.core.database import Base
import datetime


class Session(Base):
    __tablename__ = "sessions"
    
    id = Column()
    source_url = Column(String, nullable=True)
    processing_started_at = Column(DateTime, nullable=True)
    processing_finished_at = Column(DateTime, nullable=True)
    statement_count = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    
    
    statements = relationship("Statement", back_populates="session")
    processing_logs = relationship("ProcessingLog", back_populates="session")
    
    def __repr__(self):
        return f"<Session(date={self.session_date}, vol={self.volume}, num={self.number}, source_url={self.source_url}, status='{self.status}', statement_count={self.statement_count})>"
    
    