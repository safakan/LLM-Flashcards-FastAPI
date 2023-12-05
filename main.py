from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.web import router as web_router
from database.database import Base, engine
import dotenv

dotenv.load_dotenv()


app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
    "https://cards.safakan.com"  # Allow
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(web_router)
