from fastapi import APIRouter
from repository.class_repository import ClassRepository
from model.schemas import ClassCreate

router = APIRouter(prefix="/classes")
repo = ClassRepository()

@router.get("/")
async def get_all():
    return await repo.get_all()

@router.post("/")
async def create(class_: ClassCreate):
    return await repo.create(class_)

@router.delete("/{id}")
async def delete(id: str):
    return await repo.delete(id)
