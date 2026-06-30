from pydantic import BaseModel, Field


class Character(BaseModel):
    name: str
    role: str
    personality: str
    appearance: str
    abilities: list[str] = Field(default_factory=list)
    background: str