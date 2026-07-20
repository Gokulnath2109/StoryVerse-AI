from pydantic import BaseModel, Field


class GameState(BaseModel):
    health: int = 100
    mana: int = 50
    level: int = 1
    experience: int = 0
    gold: int = 0
    danger_level: int = 0

    inventory: list[str] = Field(default_factory=list)
    quests: list[str] = Field(default_factory=list)
    companions: list[str] = Field(default_factory=list)

    relationships: dict[str, int] = Field(default_factory=dict)