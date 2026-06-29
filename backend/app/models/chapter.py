from pydantic import BaseModel
from typing import List
from app.models.choice import Choice

class Chapter(BaseModel):
    chapter_number: int
    title: str
    content: str

    choices: List[Choice] = []