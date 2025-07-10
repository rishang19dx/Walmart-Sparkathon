from sqlmodel import SQLModel, Field
from datetime import datetime

class Consent(SQLModel, table=True):
    user_id: str = Field(foreign_key="user.id", primary_key=True)
    status: str
    timestamp: datetime 