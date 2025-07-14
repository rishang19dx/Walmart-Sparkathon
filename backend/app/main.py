from fastapi import FastAPI
from .api import products, chat, users, weather # Import the new routers
from sqlmodel import SQLModel
from app.models.db import sql_engine
from app.models import user, session, consent
from app.api import products
from app.api import did
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    title="Sparkathon API",
    description="API for the AI-powered personal shopping assistant with an AR-based virtual try-on system.",
    version="0.1.0"
)

# CORS middleware block (no extra indent)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Or ["*"] for all origins (less secure)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers from your api files
app.include_router(products.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(weather.router, prefix="/api")
app.include_router(did.router)  # Register the DID router
app.include_router(products.router)
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
    SQLModel.metadata.create_all(sql_engine)

init_db()