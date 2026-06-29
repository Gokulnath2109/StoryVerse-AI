from pydantic import BaseModel


class Choice(BaseModel):
    id: str
    text: str
    next_chapter: int
    consequence: str