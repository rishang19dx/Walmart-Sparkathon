from pydantic import BaseModel
from typing import Optional, Dict, Any

class User(BaseModel):
    id: str
    name: str
    did: str  # Decentralized Identifier (Polygon ID)
    ceramic_stream_id: Optional[str] = None  # Ceramic profile document reference
    preferences: Optional[Dict[str, Any]] = None
