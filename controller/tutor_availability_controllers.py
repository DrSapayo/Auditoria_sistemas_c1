from fastapi import APIRouter
from repository.tutor_availability_repository import AvailabilityRepository
from model.schemas import AvailabilityCreate, AvailabilityUpdate
from fastapi import HTTPException

router = APIRouter(prefix="/availability")
repo = AvailabilityRepository()

@router.get("/")
async def get_all():
    return await repo.get_all()

@router.post("/")
async def create(availability: AvailabilityCreate):
    return await repo.create(availability)

@router.put("/{id}")
async def update(id: str, availability: AvailabilityUpdate):
    updated = await repo.update(
        id,
        availability.model_dump(exclude_unset=True)
    )
    if updated['modified_count'] == 0:
        raise HTTPException(status_code=404, detail="User not found or no changes made")
    
    return {"message": "User updated successfully"}