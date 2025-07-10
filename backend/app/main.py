from fastapi import FastAPI
from .api import products, chat, users, weather # Import the new routers
from sqlmodel import SQLModel
from app.models.db import engine
from app.models import user, session, consent


app = FastAPI(
    title="Sparkathon API",
    description="API for the AI-powered personal shopping assistant with an AR-based virtual try-on system.",
    version="0.1.0"
)

# Include the routers from your api files
app.include_router(products.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(weather.router, prefix="/api")
app.include_router(did.router)  # Register the DID router

@app.get("/", tags=["Root"])
async def read_root():
    """
    Root endpoint for the Sparkathon API.
    """
    return {"message": "Welcome to the Sparkathon API! Navigate to /docs for API documentation."}

"""
API Endpoints:
- /api/products: Product catalog CRUD & search (Pinecone)
- /api/users: User management, preferences, DID auth
- /api/sessions: Session management
- /api/chat: Chat endpoints
"""

def init_db():
    SQLModel.metadata.create_all(engine)

init_db()