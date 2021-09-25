from app.database.db import SessionLocal

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()