import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OLLAMA_API_URL: str = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")

settings = Settings()