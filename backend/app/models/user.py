import json
from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str
    did: str  # Decentralized Identifier (Polygon ID)
    ceramic_stream_id: Optional[str] = None  # Ceramic profile document reference
    preferences: Optional[str] = None  # Store as JSON string

    def get_preferences(self):
        return json.loads(self.preferences) if self.preferences else {}

    def set_preferences(self, prefs: dict):
        self.preferences = json.dumps(prefs)
