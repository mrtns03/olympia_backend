import sqlite3

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer

from auth import get_password_hash, create_access_token, get_user

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/users")
async def create_user(*, username: str, password: str, token: str = Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    hashed_password = get_password_hash(password)
    session.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, hashed_password))
    session.commit()
    user = get_user(username)
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}