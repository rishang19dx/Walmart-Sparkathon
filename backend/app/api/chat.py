from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ollama_service import get_ollama_response

class ChatQuery(BaseModel):
    query: str
    user_id: str # To maintain conversation context in the future

class ChatResponse(BaseModel):
    response: str

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatQuery):
    try:
        response = get_ollama_response(request.query)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))