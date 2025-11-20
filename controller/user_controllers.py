from fastapi import APIRouter
from repository.user_repository import UserRepository
from model.schemas import User

router = APIRouter(prefix="/users")
repo = UserRepository()

@router.get("/")
async def get_users():
    return await repo.get_all()

@router.post("/")
async def create_user(user: User):
    return await repo.create(user)
