from fastapi import APIRouter
from repository.class_repository import ClassRepository
from model.schemas import Class

router = APIRouter(prefix="/classes")
repo = ClassRepository()

@router.get("/")
async def get_all():
    return await repo.get_all()

@router.post("/")
async def create(class_: Class):
    return await repo.create(class_)
