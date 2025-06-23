from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from app.models.mp import MP
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG)

def seed_data():
    print("Seeding initial data")
    with Session(engine) as db:
        
        initial_mps = [
            {
                "full_name": "Jacob Mudenda",
                "honorific": "The Hon Speaker",
                "party": "ZANU-PF", 
                "constituency": "N/A",
                "biography": "Jacob Mudenda is the Speaker of the National Assembly of Zimbabwe.",
                "is_active": True
            },
            {
                "full_name": "Scott Sakupwanya",
                "honorific": "Hon",
                "party": "ZANU-PF", 
                "constituency": "Mabvuku",
                "biography": "Jacob Mudenda is the Speaker of the National Assembly of Zimbabwe.",
                "is_active": True
            },
            {
                "full_name": "Felix Mhona",
                "honorific": "Minister of Transport",
                "party": "ZANU-PF", 
                "constituency": "Chikomba Central",
                "biography": "Jacob Mudenda is the Speaker of the National Assembly of Zimbabwe.",
                "is_active": True
            },
            {
                "full_name": "Takudzwa Ngadziore",
                "honorific": "Hon",
                "party": "CCC", 
                "constituency": "N/A",
                "biography": "Jacob Mudenda is the Speaker of the National Assembly of Zimbabwe.",
                "is_active": True
            },
            {
                "full_name": "Agency Gumbo",
                "honorific": "The Hon Speaker",
                "party": "CCC", 
                "constituency": "Hatcliffe",
                "biography": "Jacob Mudenda is the Speaker of the National Assembly of Zimbabwe.",
                "is_active": True
            },
            {
                "full_name": "Discent Collins Bajila",
                "honorific": "Hon",
                "party": "CCC", 
                "constituency": "Luveve",
                "biography": "Jacob Mudenda is the Speaker of the National Assembly of Zimbabwe.",
                "is_active": True
            },
            {
                "full_name": "Tendai Biti",
                "honorific": "Hon.",
                "party": "CCC",
                "constituency": "Harare East",
                "biography": "Jacob Mudenda is the Speaker of the National Assembly of Zimbabwe.",
                "is_active": False,
            }
        ]
        
        for mp in initial_mps:
            existing_mp = db.query(MP).filter(MP.full_name == mp["full_name"]).first()
            if not existing_mp:
                print(f"Adding MP: {mp['full_name']}")
                mp = MP(**mp)
                db.add(mp)
            else:
                print(f"MP {mp['full_name']} already exists, skipping.")
            
        db.commit()
        print("Seeding complete.")
        
if __name__ == "__main__":
    seed_data()
    
    