from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    full_name: str | None = None

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
