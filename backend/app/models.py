from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(..., unique=True)
    email: str = Field(..., unique=True)
    password: str
    
