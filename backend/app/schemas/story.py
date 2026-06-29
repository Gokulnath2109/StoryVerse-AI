from pydantic import BaseModel

class StoryRequest(BaseModel):
    title: str
    genre: str
    style: str
    length: str