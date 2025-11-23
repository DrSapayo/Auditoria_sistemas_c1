from bson import ObjectId
from model.schemas import UserCreate
from database.database import db
from datetime import timezone, datetime
from util.security import hash_password

collection = db["user"]

class UserRepository:
    async def get_all(self):
        users = []
        async for doc in collection.find():
            doc["_id"] = str(doc["_id"])
            users.append(doc)
        return users

    async def create(self, user: UserCreate):
        document = user.model_dump(by_alias=True)
        document['password'] = hash_password(document['password'])  # Simulate password hashing
        document['created_at'] = datetime.now(timezone.utc)
        result = await collection.insert_one(document)
        return {"id": str(result.inserted_id)}

    async def get_by_id(self, id: str):
        doc = await collection.find_one({"_id": ObjectId(id)})
        if doc:
            doc["_id"] = str(doc["_id"])
        return doc
    
    async def update(self, id: str, user_data: dict):
        update_data = {k: v for k, v in user_data.items() if v is not None}
        if 'password' in update_data:
            update_data['password'] = hash_password(update_data['password'])  # Simulate password hashing
        result = await collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": update_data}
        )
        return {"modified_count": result.modified_count}
    
    async def delete(self, id: str):
        result = await collection.delete_one({"_id": ObjectId(id)})
        return {"deleted_count": result.deleted_count}
