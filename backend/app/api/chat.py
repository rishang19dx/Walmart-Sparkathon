from fastapi import APIRouter, HTTPException, Depends, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.services.ollama_service import get_ollama_response
from app.services.pinecone_service import query_product_vectors
from ..models.session import Session as SessionModel
from ..models.db import get_session
from ..models.user import User
from ..models.consent import Consent
from sqlmodel import Session
from datetime import datetime
from typing import Dict, Any
from sentence_transformers import SentenceTransformer
import whisper
from gtts import gTTS
import os
import httpx

# In-memory cache for Ceramic profiles (keyed by user_id)
ceramic_profile_cache = {}

class ChatQuery(BaseModel):
    query: str
    user_id: str # To maintain conversation context in the future

class ChatResponse(BaseModel):
    response: str
    products: list = []

router = APIRouter()

# Load embedding model once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
# Load Whisper model once
whisper_model = whisper.load_model("base")

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatQuery, session: Session = Depends(get_session)):
    try:
        # Fetch user and consent from DB
        user = session.get(User, request.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        consent = session.get(Consent, request.user_id)
        if not consent or consent.status != "granted":
            raise HTTPException(status_code=403, detail="Consent not granted")

        # Fetch and cache Ceramic profile if not already cached for this user
        if request.user_id not in ceramic_profile_cache:
            async with httpx.AsyncClient() as client:
                resp = await client.get(f"http://localhost:3001/profile/{user.ceramic_stream_id}")
                if resp.status_code != 200:
                    raise HTTPException(status_code=500, detail=f"Ceramic profile fetch failed: {resp.text}")
                ceramic_profile_cache[request.user_id] = resp.json()
        profile = ceramic_profile_cache[request.user_id]

        # Generate real embedding for the user's query
        query_embedding = embedding_model.encode(request.query).tolist()
        pinecone_results = query_product_vectors(query_embedding, top_k=3)
        products = [match["metadata"] for match in pinecone_results]

        # Construct prompt
        prompt = f"User profile: {profile}. Query: {request.query}. Product context: {products}"
        response = get_ollama_response(prompt)
        return ChatResponse(response=response, products=products)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat/voice", response_model=ChatResponse)
async def chat_voice(user_id: str, file: UploadFile = File(...), session: Session = Depends(get_session)):
    # Save uploaded audio file temporarily
    audio_path = f"/tmp/{file.filename}"
    with open(audio_path, "wb") as f:
        f.write(await file.read())
    # Transcribe audio
    result = whisper_model.transcribe(audio_path)
    text = result["text"]
    if isinstance(text, list):
        text = " ".join(text)
    # Call the main chat endpoint with the transcribed text
    return await chat_endpoint(ChatQuery(query=text, user_id=user_id), session)

@router.get("/chat/tts")
async def chat_tts(text: str):
    tts = gTTS(text)
    audio_path = "/tmp/tts_output.mp3"
    tts.save(audio_path)
    return FileResponse(audio_path, media_type="audio/mpeg", filename="response.mp3")