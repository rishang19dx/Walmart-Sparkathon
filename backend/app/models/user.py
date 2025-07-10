from sqlmodel import SQLModel, Field
from typing import Optional, Dict, Any

class User(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str
    did: str  # Decentralized Identifier (Polygon ID)
    ceramic_stream_id: Optional[str] = None  # Ceramic profile document reference
    preferences: Optional[Dict[str, Any]] = None
