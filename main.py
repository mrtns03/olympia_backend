from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from sqlmodel import Session, create_engine
from starlette.middleware.cors import CORSMiddleware

from auth import router as auth_router
from database.olympia_database import select_ergebnisse
from database.setup import get_session

app = FastAPI()
app.include_router(auth_router)
load_dotenv()
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ergebnisse")
async def get_ergebnisse(session: Session = Depends(get_session)):
    ergebnisse = select_ergebnisse(session)
    return ergebnisse
