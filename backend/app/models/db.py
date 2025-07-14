# app/models/db.py

from pymongo import MongoClient
from app.core.config import settings 
from sqlmodel import create_engine, Session

# Create MongoDB client and access the database
client = MongoClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

# SQLModel/SQLAlchemy engine (using SQLite for example, update as needed)
sql_engine = create_engine("sqlite:///./app.db", echo=True)

def get_session():
    with Session(sql_engine) as session:
        yield session

# Optional helper to get a collection
def get_collection(name: str):
    return db[name]
