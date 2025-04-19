from sqlmodel import SQLModel, create_engine
from app.utils.config import settings

db_url = settings.DATABASE_URL

engine = create_engine(db_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)