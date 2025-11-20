from bson import ObjectId
from model.schemas import Class
from database.database import db

collection = db.classes

class ClassRepository:
    async def get_all(self):
        data = []
        async for doc in collection.find():
            doc["_id"] = str(doc["_id"])
            data.append(doc)
        return data

    async def create(self, class_: Class):
        result = await collection.insert_one(class_.dict(by_alias=True))
        return {"id": str(result.inserted_id)}
