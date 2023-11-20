from sqlalchemy import Column, Integer, String
from database.database import Base
from pydantic import BaseModel


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


# Pydantic model for the deck
class DeckResponse(BaseModel):
    id: int
    name: str 


class DeckInput(BaseModel):
    prompt: str