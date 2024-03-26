from pydantic import BaseModel, Field
from .utils import PyObjectId



class UserCreate(BaseModel):
    username: str
    user_id: int
    role: str = Field(default='common')
    is_banned: bool = Field(default=False)



class User(UserCreate):
    id: PyObjectId = Field(alias="_id")
