from fastapi import Header, HTTPException, status
from database import database as _database

async def get_db():
    if _database.db is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection is not initialized."
        )
    return _database.db

async def get_current_user(x_token: str | None = Header(None)):
    if not x_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="X-Token header missing"
        )
    session = await _database.db["sessions"].find_one({"token": x_token})
    if not session:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid X-Token"
        )
    user = await _database.db["users"].find_one({"_id": session["user_id"]})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    user["id"] = str(user["_id"])
    del user["_id"]
    return user

async def require_admin(user = None):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )  
    if user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return True