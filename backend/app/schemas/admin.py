from pydantic import BaseModel, EmailStr

class AdminCreate(BaseModel):
    email: EmailStr
    password: str

class AdminOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
