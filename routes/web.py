from fastapi import APIRouter, Request, Depends, Form, status, HTTPException
from starlette.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database.database import get_db
from auth.authentication import authenticate_user, register_user
from database.models import User, Deck, DeckInput
from database.models import DeckResponse
from typing import List
from sqlalchemy import desc
from chains.create_deck_from_input import chain_create_deck_from_input
from objects.active_deck import ActiveDeck
import json



router = APIRouter()
templates = Jinja2Templates(directory="templates")



@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(get_db)):
    user_active = False
    username = request.cookies.get("user")
    if username:
        user = db.query(User).filter(User.username == username).first()
        if user:
            user_active = True

    deck = ActiveDeck()
    current_card = deck.get_current_card() if deck.cards else None

    return templates.TemplateResponse("index.html", {
        "request": request,
        "user_active": user_active,
        "current_card": current_card
    })


@router.post("/login")
async def login_for_access_token(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        return {"status": "error", "message": "Invalid username or password"}
    
    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="user", value=username, httponly=True)
    return response

@router.get("/logout")
async def logout(request: Request, db: Session = Depends(get_db)):
    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    response.delete_cookie(key="user")
    return response

@router.post("/register")
async def register_user_endpoint(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    result = register_user(db, username, password)
    return result

@router.get("/api/decks", response_model=List[DeckResponse])
async def get_decks(db: Session = Depends(get_db)):
    decks = db.query(Deck).order_by(desc(Deck.id)).limit(15).all()
    return [DeckResponse(id=deck.id, name=deck.name) for deck in decks]


@router.post("/create_deck_from_input")
async def create_deck_from_input(deck_input: DeckInput):
    try:
        user_prompt = deck_input.prompt
        if not user_prompt:
            raise HTTPException(status_code=400, detail="No prompt provided")

        print(f"Received prompt: {user_prompt}")

        deck_data_str = chain_create_deck_from_input(user_prompt)
        print(f"Deck data received (string): {deck_data_str}")

        # Replace single quotes with double quotes to make it a valid JSON format
        deck_data_str = deck_data_str.replace("'", '"')
        print(f"Deck data string processed to be a JSON.")


        # Parse the string into a Python list of dictionaries
        deck_data = json.loads(deck_data_str)
        print(f"Deck data parsed: {deck_data}")

        # deck = ActiveDeck()
        # deck.load_deck(deck_data)
        # print("Deck loaded.")

        return {"message": "Deck created successfully", "deck": deck_data}

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/get_next_card")
async def get_next_card():
    deck = ActiveDeck()
    next_card = deck.next_card()
    return {"card": next_card}

@router.get("/get_current_card")
async def get_current_card():
    deck = ActiveDeck()
    return {"card": deck.get_current_card()}


