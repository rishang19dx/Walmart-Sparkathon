from fastapi import APIRouter, HTTPException, Request, Depends
from typing import Dict, Any
from ..models.user import User
from ..core.security import verify_did_jwt
import uuid

router = APIRouter()

# In-memory user store for demo
USERS: Dict[str, User] = {}

# In-memory consent status store for demo
CONSENT_STATUS: Dict[str, str] = {}

@router.post("/users/onboard", tags=["Users"])
async def onboard_user(name: str):
    # Mock Polygon DID and Ceramic stream creation
    user_id = str(uuid.uuid4())
    did = f"did:polygonid:{uuid.uuid4()}"
    ceramic_stream_id = f"ceramic://{uuid.uuid4()}"
    user = User(id=user_id, name=name, did=did, ceramic_stream_id=ceramic_stream_id)
    USERS[user_id] = user
    return user

@router.post("/users", tags=["Users"])
async def create_user(user: User):
    if user.id in USERS:
        raise HTTPException(status_code=400, detail="User already exists")
    USERS[user.id] = user
    return user

@router.get("/users/{user_id}", tags=["Users"])
async def get_user(user_id: str, did=Depends(verify_did_jwt)):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/{user_id}/preferences", tags=["Users"])
async def get_preferences(user_id: str, did=Depends(verify_did_jwt)):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.preferences or {}

@router.put("/users/{user_id}/preferences", tags=["Users"])
async def update_preferences(user_id: str, preferences: Dict[str, Any], did=Depends(verify_did_jwt)):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.preferences = preferences
    USERS[user_id] = user
    return user.preferences

@router.post("/users/{user_id}/consent/request", tags=["Consent"])
async def request_consent(user_id: str):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    CONSENT_STATUS[user_id] = "requested"
    return {"user_id": user_id, "consent": "requested"}

@router.post("/users/{user_id}/consent/grant", tags=["Consent"])
async def grant_consent(user_id: str):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    CONSENT_STATUS[user_id] = "granted"
    return {"user_id": user_id, "consent": "granted"}

@router.get("/users/{user_id}/consent/status", tags=["Consent"])
async def consent_status(user_id: str):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    status = CONSENT_STATUS.get(user_id, "none")
    return {"user_id": user_id, "consent": status}

@router.get("/users/{user_id}/profile", tags=["Users"])
async def get_user_profile(user_id: str):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    if CONSENT_STATUS.get(user_id) != "granted":
        raise HTTPException(status_code=403, detail="Consent not granted")
    user = USERS[user_id]
    # Mocked Ceramic profile data
    profile = {
        "ceramic_stream_id": user.ceramic_stream_id,
        "preferences": user.preferences or {},
        "history": [],  # Placeholder for style/feedback history
        "did": user.did,
        "name": user.name
    }
    return profile
