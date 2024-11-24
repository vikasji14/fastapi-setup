from typing import List, Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

users = [
    {"email": "a@b.com", "is_active": True, "bio": "Hello"},
    {"email": "c@b.com", "is_active": False, "bio": "World"},
]

class User(BaseModel):
    email: str
    is_active: bool
    bio:Optional[str]

@router.get("/")
async def get_users():
    return users

@router.post("/")
async def create_user(user: User):
    users.append(user)
    return "Success"

@router.get("/{id}")
async def getUserById(id: int):
    return {"User": users[id]}
                    