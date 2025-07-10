from fastapi import APIRouter, HTTPException, Request, Depends
from typing import Dict, Any
from ..models.user import User
from ..models.consent import Consent
from ..models.db import get_session
from ..core.security import verify_did_jwt
from sqlmodel import Session, select
import uuid
import httpx
from datetime import datetime
from eth_account.messages import encode_defunct
from eth_account import Account

CERAMIC_MICROSERVICE_URL = "http://localhost:3001"

router = APIRouter()

# @router.post("/users/onboard", tags=["Users"])
# async def onboard_user(name: str, session: Session = Depends(get_session)):
#     user_id = str(uuid.uuid4())
#     did = f"did:polygonid:{uuid.uuid4()}"  # TODO: Replace with real DID from wallet
#     profile = {"name": name, "preferences": {}, "history": []}
#     async with httpx.AsyncClient() as client:
#         resp = await client.post(f"{CERAMIC_MICROSERVICE_URL}/create-profile", json={"did": did, "profile": profile})
#         if resp.status_code != 200:
#             raise HTTPException(status_code=500, detail=f"Ceramic profile creation failed: {resp.text}")
#         ceramic_stream_id = resp.json()["streamId"]
#     user = User(id=user_id, name=name, did=did, ceramic_stream_id=ceramic_stream_id)
#     session.add(user)
#     session.commit()
#     session.refresh(user)
#     return user
# (Mock onboarding endpoint commented out for demo - use /users/onboard_wallet for real onboarding)

@router.post("/users/onboard_wallet", tags=["Users"])
async def onboard_wallet_user(address: str, challenge: str, signature: str, session: Session = Depends(get_session)):
    # 1. Verify the signature
    message = encode_defunct(text=challenge)
    try:
        recovered_address = Account.recover_message(message, signature=signature)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Signature verification failed: {str(e)}")
    if recovered_address.lower() != address.lower():
        raise HTTPException(status_code=401, detail="Signature does not match address")
    # 2. Construct the DID
    did = f"did:ethr:{address.lower()}"
    # 3. Create user and Ceramic profile as in normal onboarding
    user_id = str(uuid.uuid4())
    profile = {"name": address, "preferences": {}, "history": []}
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{CERAMIC_MICROSERVICE_URL}/create-profile", json={"did": did, "profile": profile})
        if resp.status_code != 200:
            raise HTTPException(status_code=500, detail=f"Ceramic profile creation failed: {resp.text}")
        ceramic_stream_id = resp.json()["streamId"]
    user = User(id=user_id, name=address, did=did, ceramic_stream_id=ceramic_stream_id)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.post("/users", tags=["Users"])
async def create_user(user: User, session: Session = Depends(get_session)):
    existing = session.get(User, user.id)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/users/{user_id}", tags=["Users"])
async def get_user(user_id: str, did=Depends(verify_did_jwt), session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/{user_id}/preferences", tags=["Users"])
async def get_preferences(user_id: str, did=Depends(verify_did_jwt), session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.preferences or {}

@router.put("/users/{user_id}/preferences", tags=["Users"])
async def update_preferences(user_id: str, preferences: Dict[str, Any], did=Depends(verify_did_jwt), session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.preferences = preferences
    session.add(user)
    session.commit()
    session.refresh(user)
    return user.preferences

@router.post("/users/{user_id}/consent/request", tags=["Consent"])
async def request_consent(user_id: str, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    consent = session.get(Consent, user_id)
    if not consent:
        consent = Consent(user_id=user_id, status="requested", timestamp=datetime.utcnow())
    else:
        consent.status = "requested"
        consent.timestamp = datetime.utcnow()
    session.add(consent)
    session.commit()
    return {"user_id": user_id, "consent": "requested"}

@router.post("/users/{user_id}/consent/grant", tags=["Consent"])
async def grant_consent(user_id: str, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    consent = session.get(Consent, user_id)
    if not consent:
        consent = Consent(user_id=user_id, status="granted", timestamp=datetime.utcnow())
    else:
        consent.status = "granted"
        consent.timestamp = datetime.utcnow()
    session.add(consent)
    session.commit()
    return {"user_id": user_id, "consent": "granted"}

@router.get("/users/{user_id}/consent/status", tags=["Consent"])
async def consent_status(user_id: str, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    consent = session.get(Consent, user_id)
    status = consent.status if consent else "none"
    return {"user_id": user_id, "consent": status}

@router.get("/users/{user_id}/profile", tags=["Users"])
async def get_user_profile(user_id: str, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    consent = session.get(Consent, user_id)
    if not consent or consent.status != "granted":
        raise HTTPException(status_code=403, detail="Consent not granted")
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{CERAMIC_MICROSERVICE_URL}/profile/{user.ceramic_stream_id}")
        if resp.status_code != 200:
            raise HTTPException(status_code=500, detail=f"Ceramic profile fetch failed: {resp.text}")
        profile = resp.json()
    profile["ceramic_stream_id"] = user.ceramic_stream_id
    profile["did"] = user.did
    profile["name"] = user.name
    return profile
