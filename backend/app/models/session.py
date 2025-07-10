from sqlmodel import SQLModel, Field
from typing import Optional

class Session(SQLModel, table=True):
    session_id: str = Field(primary_key=True)
    user_id: str
    created_at: Optional[str] = None 