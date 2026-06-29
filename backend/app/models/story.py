from pydantic import BaseModel
from typing import List


class Story(BaseModel):
    story_id: str
    title: str
    genre: str
    style: str
    length: str

    characters: List[str] = []

    chapters: List[str] = []

    current_chapter: int = 0

    choices: List[str] = []

    status: str = "ongoing"

    ending: str = ""