from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

MONGODB_URL = "mongodb://mongodb_container:27017"  # Use the service name defined in docker-compose
client = AsyncIOMotorClient(MONGODB_URL)
db = client.mydatabase  # Replace 'mydatabase' with your desired database name

# Create a function to get the database
async def get_database():
    return db