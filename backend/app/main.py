from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase
import bcrypt

app = FastAPI()

# Add CORS middleware
origins = [
    "http://localhost:3000",  # Your frontend's URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# User registration model
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

@app.post("/register/")
async def register_user(user: UserCreate):
    db = await get_database()
    
    # Check if the username already exists
    existing_user = await db.users.find_one({"username": user.username})
    existing_email = await db.users.find_one({"email": user.email})
    
    if existing_user or existing_email:
        raise HTTPException(status_code=400, detail="email already registered")
    
    # Hash the password
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    
    # Create the new user
    new_user = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password.decode('utf-8')
    }
    
    await db.users.insert_one(new_user)
    return {"message": "User registered successfully!"}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Retail Auction App!"}
