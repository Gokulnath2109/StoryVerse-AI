from pydantic import BaseModel

class Choice(BaseModel):
    id: str
    text: str