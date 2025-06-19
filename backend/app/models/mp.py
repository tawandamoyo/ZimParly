from sqlalchemy import Column, Index, String, Text,ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class MP(Base):
    __tablename__ = "mps"
    
    full_name = Column(String(255), nullable=False, index=True)
    honorific = Column(String(50))
    party = Column(String(255), index=True)
    constituency = Column(String(255), index=True)
    biography = Column(Text)
    is_active = Column(Boolean, default=True, nullable=False, index=True)
    statements = relationship("Statement", back_populates="speaker")
    
    __table_args__ = (
        Index('idx_mp_name_active', 'full_name', 'is_active'),
        Index('idx_mp_party_active', 'party', 'is_active'),
    )
    
    def __repr__(self):
        return f"<MP(full_name={self.full_name}, party={self.party}, constituency={self.constituency})>"
    
    @property
    def display_name(self):
        return f"{self.honorific} {self.full_name}" if self.honorific else self.full_name
    
    