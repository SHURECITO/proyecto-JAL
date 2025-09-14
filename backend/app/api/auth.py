from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta, timezone
from ..core.config import settings
from ..services.security import pwd_context

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login", response_model=Token)
async def login(payload: LoginRequest):
    if payload.email != settings.ADMIN_EMAIL:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if settings.ADMIN_PASSWORD_HASH:
        if not pwd_context.verify(payload.password, settings.ADMIN_PASSWORD_HASH):
            raise HTTPException(status_code=401, detail="Invalid credentials")
    else:
        if payload.password != settings.ADMIN_PASSWORD:
            raise HTTPException(status_code=401, detail="Invalid credentials")

    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": settings.ADMIN_EMAIL, "exp": expire}
    token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")

    return {"access_token": token, "token_type": "bearer"}
