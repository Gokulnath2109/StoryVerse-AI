from pydantic import BaseModel


class Character(BaseModel):
    name: str
    role: str
    personality: str
    appearance: str
    abilities: list[str] = []
    background: str