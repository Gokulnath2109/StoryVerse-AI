from pydantic import BaseModel
from typing import List


class Chapter(BaseModel):
    chapter_number: int
    title: str
    content: str

    choices: List[str] = []