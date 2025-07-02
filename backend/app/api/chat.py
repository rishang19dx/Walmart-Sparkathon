from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.ollama_service import get_ollama_response
from ..models.session import Session
from datetime import datetime
from typing import Dict
from ..api.users import USERS, CONSENT_STATUS

class ChatQuery(BaseModel):
    query: str
    user_id: str # To maintain conversation context in the future

class ChatResponse(BaseModel):
    response: str

router = APIRouter()

SESSIONS: Dict[str, Session] = {}

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatQuery):
    try:
        # Fetch user profile if consent is granted
        user = USERS.get(request.user_id)
        profile = None
        if user and CONSENT_STATUS.get(request.user_id) == "granted":
            profile = {
                "preferences": user.preferences or {},
                "did": user.did,
                "name": user.name
            }
        # Construct prompt
        if profile:
            prompt = f"User profile: {profile}. Query: {request.query}"
        else:
            prompt = request.query
        response = get_ollama_response(prompt)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/sessions", tags=["Sessions"])
async def create_session(user_id: str):
    session_id = f"sess_{len(SESSIONS)+1}"
    session = Session(session_id=session_id, user_id=user_id, created_at=datetime.utcnow())
    SESSIONS[session_id] = session
    return session

@router.get("/sessions/{session_id}", tags=["Sessions"])
async def get_session(session_id: str):
    session = SESSIONS.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session