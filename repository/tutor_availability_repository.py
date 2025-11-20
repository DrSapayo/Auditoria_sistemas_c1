from bson import ObjectId
from model.schemas import TutorAvailability
from database.database import db

collection = db.tutor_availability

class AvailabilityRepository:
    async def get_all(self):
        data = []
        async for doc in collection.find():
            doc["_id"] = str(doc["_id"])
            data.append(doc)
        return data

    async def create(self, availability: TutorAvailability):
        result = await collection.insert_one(availability.dict(by_alias=True))
        return {"id": str(result.inserted_id)}
