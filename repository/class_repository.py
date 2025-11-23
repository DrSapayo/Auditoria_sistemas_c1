from bson import ObjectId
from model.schemas import ClassCreate
from database.database import db
from datetime import timezone, datetime

collection = db["classes"]

class ClassRepository:
    async def get_all(self):
        data = []
        async for doc in collection.find():
            doc["_id"] = str(doc["_id"])
            data.append(doc)
        return data

    async def create(self, class_: ClassCreate):
        data = class_.model_dump(by_alias=True)
        data['created_at'] = datetime.now(timezone.utc)
        result = await collection.insert_one(data)
        return {"id": str(result.inserted_id)}
    
    async def delete(self, id: str):
        result = await collection.delete_one({"_id": ObjectId(id)})
        return {"deleted_count": result.deleted_count}
