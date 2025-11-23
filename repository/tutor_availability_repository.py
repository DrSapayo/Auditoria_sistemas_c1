from bson import ObjectId
from model.schemas import AvailabilityCreate
from database.database import db

collection = db["tutor_availability"]

class AvailabilityRepository:
    async def get_all(self):
        data = []
        async for doc in collection.find():
            doc["_id"] = str(doc["_id"])
            data.append(doc)
        return data

    async def create(self, availability: AvailabilityCreate):
        data = availability.model_dump(by_alias=True)
        result = await collection.insert_one(data)
        return {"id": str(result.inserted_id)}
    
    async def update(self, id: str, availability_data: dict):
        update_data = {k: v for k, v in availability_data.items() if v is not None}
        result = await collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": update_data}
        )
        return {"modified_count": result.modified_count}
