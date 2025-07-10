from fastapi import APIRouter, HTTPException, Query
from app.services import did_service

router = APIRouter(prefix="/did", tags=["DID"])

@router.post("/generate", summary="Generate a new DID and key")
def generate_did():
    try:
        result = did_service.generate_did_key()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/resolve", summary="Resolve a DID to its DID Document")
def resolve_did(did: str = Query(..., description="The DID to resolve")):
    try:
        did_document = did_service.resolve_did(did)
        return {"did_document": did_document}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
