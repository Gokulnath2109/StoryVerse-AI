from pydantic import BaseModel
from typing import List
from app.models.chapter import Chapter

class Story(BaseModel):
    story_id: str
    title: str
    genre: str
    style: str
    length: str

    characters: List[str] = []

    chapters: List[Chapter] = []

    current_chapter: int = 1

    choices: List[str] = []

    status: str = "ongoing"

    ending: str = ""