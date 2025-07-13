import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OLLAMA_API_URL: str = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY", "")
    PINECONE_ENV: str = os.getenv("PINECONE_ENV", "us-east-1 ")
    PINECONE_INDEX: str = os.getenv("PINECONE_INDEX", "products-index")
    DID_RESOLVER_URL: str = os.getenv("DID_RESOLVER_URL", "https://uniresolver.io/1.0/identifiers/")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "chatbot_db")
settings = Settings()