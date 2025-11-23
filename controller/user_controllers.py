from fastapi import APIRouter
from repository.user_repository import UserRepository
from model.schemas import UserCreate, UserUpdate
from fastapi import HTTPException

router = APIRouter(prefix="/users")
repo = UserRepository()

@router.get("/")
async def get_users():
    return await repo.get_all()

@router.post("/")
async def create_user(user: UserCreate):
    return await repo.create(user)

@router.put("/{id}")
async def update_user(id: str, user: UserUpdate):
    updated = await repo.update(
        id,
        user.model_dump(exclude_unset=True)
    )
    if updated['modified_count'] == 0:
        raise HTTPException(status_code=404, detail="User not found or no changes made")
    
    return {"message": "User updated successfully"}

@router.delete("/{id}")
async def delete_user(id: str):
    return await repo.delete(id)