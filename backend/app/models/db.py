# app/models/db.py

from pymongo import MongoClient
from app.core.config import settings 

# Create MongoDB client and access the database
client = MongoClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

# Optional helper to get a collection
def get_collection(name: str):
    return db[name]
