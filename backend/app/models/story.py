from pydantic import BaseModel, Field
from typing import List

from app.models.chapter import Chapter
from app.models.character import Character
from app.models.game_state import GameState


class Story(BaseModel):
    # Story Information
    story_id: str
    title: str
    genres: List[str]
    total_chapters: int

    # Characters
    characters: List[Character] = Field(default_factory=list)

    # Player Game State
    game_state: GameState = Field(default_factory=GameState)

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

    active_event: dict | None = None

    # Risk Warning (Version 2)
    warning_message: str | None = None