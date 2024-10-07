# backend/app/crud.py

from fastapi import APIRouter
from .models import AuctionItem
from .database import db

router = APIRouter()

@router.post("/items/")
async def create_auction_item(item: AuctionItem):
    result = await db.auction_items.insert_one(item.dict())
    return {"id": str(result.inserted_id)}

@router.get("/items/")
async def read_auction_items():
    items = []
    async for item in db.auction_items.find():
        items.append(item)
    return items