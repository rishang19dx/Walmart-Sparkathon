from fastapi import FastAPI
from .api import products, chat # Import the new routers

app = FastAPI(
    title="Sparkathon API",
    description="API for the AI-powered personal shopping assistant with an AR-based virtual try-on system.",
    version="0.1.0"
)

# Include the routers from your api files
app.include_router(products.router, prefix="/api")
app.include_router(chat.router, prefix="/api")

@app.get("/", tags=["Root"])
async def read_root():
    """
    Root endpoint for the Sparkathon API.
    """
    return {"message": "Welcome to the Sparkathon API! Navigate to /docs for API documentation."}