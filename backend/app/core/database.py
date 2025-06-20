"""
Database configuration and base models.
"""

from sqlalchemy import create_engine, Column, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
from typing import Generator

from .config import settings

# Database engine configuration
engine = create_engine(
    settings.DATABASE_URL,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    echo=settings.DEBUG,  # Log SQL queries in debug mode
    # For SQLite compatibility in development
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {},
    poolclass=StaticPool if "sqlite" in settings.DATABASE_URL else None,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base for all models
Base = declarative_base()


class TimestampMixin:
    """Mixin to add created_at and updated_at timestamps to models."""
    
    @declared_attr
    def created_at(cls):
        return Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime(timezone=True), 
            server_default=func.now(), 
            onupdate=func.now(), 
            nullable=False
        )


class BaseModel(Base, TimestampMixin):
    """Base model class that includes common fields."""
    
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"


# Database dependency for FastAPI
def get_db() -> Generator[Session, None, None]:
    """
    Database session dependency.
    
    Yields a database session that will be automatically closed
    after the request is complete.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Database initialization functions
def create_tables():
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)


def drop_tables():
    """Drop all database tables. Use with caution!"""
    Base.metadata.drop_all(bind=engine)