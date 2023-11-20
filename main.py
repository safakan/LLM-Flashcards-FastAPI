from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.web import router as web_router
from database.database import Base, engine
import dotenv

dotenv.load_dotenv()


app = FastAPI()

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(web_router)