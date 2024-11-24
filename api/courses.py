from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
    responses={404: {"description": "Not found"}}
)

courses = [
    {"name": "a", "description": "b"},
    {"name": "c", "description": "d"},
]


@router.get("/")
async def get_courses():
    return {"courses": []}

@router.post("/")
async def create_course(course: dict):
    courses.append(course)
    return "Success"


@router.get("/{id}")
async def read_course(id: int):
    return {"courses": []}

@router.patch("/{id}")
async def update_course(id: int, course: dict):
    return {"courses": []}

@router.delete("/{id}")
async def delete_course(id: int):
    return {"courses": []}


@router.get("/{id}/sections")
async def read_course_sections(id: int):
    return {"courses": []}

@router.get("/{id}/sections/{section_id}")
async def read_section(id: int, section_id: int):
    return {"courses": []}

@router.get("/{id}/sections/{section_id}/contents-block")
async def read_section_contents_block(id: int, section_id: int):
    return {"courses": []}

@router.get("/{id}/sections/{section_id}/contents-block/{content_block_id}")
async def read_content_block(id: int, section_id: int, content_block_id: int):
    return {"courses": []}