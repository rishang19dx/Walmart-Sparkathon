from sqlmodel import SQLModel, create_engine, Session
from contextlib import contextmanager

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, echo=True)

# Dependency for FastAPI endpoints
def get_session():
    with Session(engine) as session:
        yield session 