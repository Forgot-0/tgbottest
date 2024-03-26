from pydantic import BaseModel, Field



class UserDogCreate(BaseModel):
    user_id: int
    dog_info: str