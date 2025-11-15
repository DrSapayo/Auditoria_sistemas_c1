from bson import ObjectId

class UserRepository:
    def __init__(self, db):
        self._db = db
        self._collection = self._db["users"]

    async def create(self, user_data: dict) -> str:
        result = await self._collection.insert_one(user_data)
        return str(result.inserted_id)
    
    async def get_by_email(self, email: str) -> dict:
        return await self._collection.find_one({"email": email})
    
    async def get_by_id(self, user_id: str) -> dict:
        return await self._collection.find_one({"_id": ObjectId(user_id)})
    
    async def list(self, filter: dict = {}, limit: int = 50, skip: int = 0) -> list:
        cursor = self._collection.find(filter).skip(skip).limit(limit)
        items = []
        async for document in cursor:
            document["id"] = str(document["_id"])
            del document["_id"]
            items.append(document)
        return items
    
    async def update_role(self, id: str, new_role: str) -> dict:
        await self._collection.update_one(
            {"_id": ObjectId(id)}, 
            {"$set": {"role": new_role}}
            )
        return await self.get_by_id(id)