from bson import ObjectId
from model.schemas import User
from database.database import db

collection = db["user"]

class UserRepository:
    async def get_all(self):
        users = []
        async for doc in collection.find():
            doc["_id"] = str(doc["_id"])
            users.append(doc)
        return users

    async def create(self, user: User):
        data = user.model_dump(by_alias=True)
        result = await collection.insert_one(data)
        return {"id": str(result.inserted_id)}

    async def get_by_id(self, id: str):
        doc = await collection.find_one({"_id": ObjectId(id)})
        if doc:
            doc["_id"] = str(doc["_id"])
        return doc
