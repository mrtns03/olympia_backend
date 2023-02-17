from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from auth import router as auth_router
from admin import router as admin_router
from database.olympia_database import select_ergebnisse, select_athletes, select_athletes_by_nation

app = FastAPI()
app.include_router(auth_router)
app.include_router(admin_router)
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
async def root():
    ergebnisse = select_ergebnisse()
    return ergebnisse


@app.get("/athleten")
async def root():
    athletes = select_athletes()
    return athletes

@app.get("/athleten/{nation}")
async def root(nation: str):
    athletes = select_athletes_by_nation(nation)
    return athletes
