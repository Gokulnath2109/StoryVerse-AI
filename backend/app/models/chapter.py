from pydantic import BaseModel, Field
from typing import List
from app.models.scene import Scene


class Chapter(BaseModel):
    chapter_number: int
    title: str
    scenes: List[Scene] = Field(default_factory=list)