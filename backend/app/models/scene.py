from pydantic import BaseModel, Field
from typing import List
from app.models.choice import Choice


class Scene(BaseModel):
    scene_number: int
    content: str
    choices: List[Choice] = Field(default_factory=list)