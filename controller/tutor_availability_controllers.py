from fastapi import APIRouter
from repository.tutor_availability_repository import AvailabilityRepository
from model.schemas import TutorAvailability

router = APIRouter(prefix="/availability")
repo = AvailabilityRepository()

@router.get("/")
async def get_all():
    return await repo.get_all()

@router.post("/")
async def create(availability: TutorAvailability):
    return await repo.create(availability)
