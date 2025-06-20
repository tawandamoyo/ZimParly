from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "ZimParliamentWatch"
    DEBUG: bool = False
    
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int
    DATABASE_MAX_OVERFLOW: int
    
    OPENSEARCH_URL: str
    OPENSEARCH_INDEX: str
    
    REDIS_URL: str
    
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    
    PARLIAMENT_BASE_URL: str
    SCRAPING_DELAY: int  
    
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        
settings = Settings()