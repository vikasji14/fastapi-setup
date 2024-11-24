from typing import List, Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/sections",
    tags=["sections"],
    responses={404: {"description": "Not found"}}
)

sections = [
    {"name": "a", "description": "b"},
    {"name": "c", "description": "d"},
]

@router.get("/{id}")
async def read_section(id: int):
    return {"courses":[]}

@router.get("/{id}/contents-block")
async def read_sections_contents_block():
    return {"courses": []}

@router.get("/content-blocks/{id}")
async def read_content_block(id: int):
    return {"courses": []}

