from pydantic import BaseModel, Field
from typing import List

from app.models.chapter import Chapter
from app.models.character import Character


class Story(BaseModel):
    # Story Information
    story_id: str
    title: str
    genres: List[str]
    total_chapters: int

    # Characters
    characters: List[Character] = Field(default_factory=list)

    # Generated Chapters
    chapters: List[Chapter] = Field(default_factory=list)

    # Current Progress
    current_chapter: int = 1
    current_scene: int = 1

    # User Choice History
    choice_history: List[str] = Field(default_factory=list)

    # Story Status
    status: str = "ongoing"

    # Story Ending
    ending: str = ""