from bson import ObjectId
from datetime import datetime, timezone

class PurchaseRepository:
    def __init__(self, db):
        self._db = db
        self._collection = self._db["purchases"]

    async def create(self, purchase_data: dict) -> str:
        purchase_data.setdefault("purchased_at", datetime.now(timezone.utc))
        result = await self._collection.insert_one(purchase_data)
        return str(result.inserted_id)
    
    async def list_by_user(self, user_id:str) -> list:
        cursor = self._collection.find({"user_id": user_id})
        items = []
        async for document in cursor:
            document["id"] = str(document["_id"])
            del document["_id"]
            items.append(document)
        return items