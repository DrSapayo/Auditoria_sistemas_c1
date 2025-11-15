from bson import ObjectId

class BookRepository:
    def __init__(self, db):
        self._db = db
        self._collection = self._db["books"]

    async def create(self, book_data: dict) -> str:
        result = await self._collection.insert_one(book_data)
        return str(result.inserted_id)
    
    async def find(self, filter: dict = {}, limit: int = 50, skip: int = 0) -> list:
        cursor = self._collection.find(filter).skip(skip).limit(limit)
        items = []
        async for document in cursor:
            document["id"] = str(document["_id"])
            del document["_id"]
            items.append(document)
        return items
    
    async def find_by_id(self, book_id: str) -> dict:
        doc = await self._collection.find_one({"_id": ObjectId(book_id)})
        if doc:
            doc["id"] = str(doc["_id"])
            del doc["_id"]
        return doc
    
    async def update(self, book_id: str, update_data: dict) -> dict:
        await self._collection.update_one(
            {"_id": ObjectId(book_id)},
            {"$set": update_data}
        )
        return await self.find_by_id(book_id)
    
    async def delete(self, book_id: str) -> bool:
        result = await self._collection.delete_one({"_id": ObjectId(book_id)})
        return result.deleted_count == 1