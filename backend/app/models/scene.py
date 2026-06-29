from pydantic import BaseModel
from typing import List
from app.models.choice import Choice


class Scene(BaseModel):
    scene_number: int
    content: str
    choices: List[Choice] = []