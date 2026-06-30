from pydantic import BaseModel
from typing import List


class StoryRequest(BaseModel):
    title: str
    chapters: int
    genres: List[str]
    character_mode: str   # "auto" or "custom"
    characters: List[str] = []