from pydantic import BaseModel
from datetime import datetime

class Session(BaseModel):
    session_id: str
    user_id: str
    created_at: datetime
    is_active: bool = True 