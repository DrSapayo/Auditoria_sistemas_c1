from passlib.context import CryptContext
import secrets
from datetime import datetime, timezone, timedelta

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def generate_token() -> str:
    return secrets.token_urlsafe(32)

def token_expiration(hours: int = 1) -> datetime:
    return datetime.now(timezone.utc) + timedelta(hours=hours)  