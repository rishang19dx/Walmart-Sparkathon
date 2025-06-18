from fastapi import APIRouter
from pydantic import BaseModel

class ChatQuery(BaseModel):
    query: str
    user_id: str # To maintain conversation context in the future

class ChatResponse(BaseModel):
    response: str

router = APIRouter()

@router.post("/chat/style", response_model=ChatResponse, tags=["Chat"])
async def get_style_suggestion(query: ChatQuery):
    """
    Accepts a user query and returns a basic, hardcoded style suggestion.
    This fulfills the Week 1 goal of testing a simple conversational flow.
    """
    # In Week 2, this will be replaced with a call to the Ollama service.
    mock_response = f"Based on your query for '{query.query}', I suggest our Classic Crewneck T-Shirt and High-Rise Skinny Jeans."
    return {"response": mock_response}