from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", 1440))

if not JWT_SECRET:
    raise ValueError("JWT_SECRET environment variable is not set")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Baza użytkowników w pamięci
users_db = []


def register_user(email: str, password: str) -> dict:
    existing = next((u for u in users_db if u["email"] == email), None)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Użytkownik z tym emailem już istnieje"
        )

    hashed_password = pwd_context.hash(password)
    new_user = {
        "id": len(users_db) + 1,
        "email": email,
        "password": hashed_password
    }
    users_db.append(new_user)
    return {"id": new_user["id"], "email": new_user["email"]}


def login_user(email: str, password: str) -> dict:
    user = next((u for u in users_db if u["email"] == email), None)
    if not user or not pwd_context.verify(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nieprawidłowy email lub hasło"
        )

    expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_MINUTES)
    token = jwt.encode(
        {"id": user["id"], "email": user["email"], "exp": expire},
        JWT_SECRET or "",
        algorithm=JWT_ALGORITHM
    )
    return {"token": token, "token_type": "bearer"}
