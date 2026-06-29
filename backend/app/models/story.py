from pydantic import BaseModel
from typing import List
from app.models.chapter import Chapter
from app.models.character import Character

class Story(BaseModel):
    story_id: str
    title: str
    genre: str
    style: str
    length: str

    characters: List[Character] = []

    chapters: List[Chapter] = []

    current_chapter: int = 1

    status: str = "ongoing"

    ending: str = ""