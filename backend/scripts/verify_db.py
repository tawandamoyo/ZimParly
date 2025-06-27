
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from app.models.mp import MP
from app.core.config import settings

def verify_connection():
    try:
        engine = create_engine(settings.DATABASE_URL)
        with Session(engine) as db:
            print("Database connection successful")
            mp_count = db.query(MP).count()
            print(f"Total MPs in database: {mp_count}")
            
            first_mp = db.query(MP).first()
            if first_mp:
                print(f"First MP in database: {first_mp.full_name} ({first_mp.party})")
            else:
                print("No MPs found in the database.")
                
    except Exception as e:
        print(f"Database connection failed: {e}")
    
if __name__ == "__main__":
        verify_connection()