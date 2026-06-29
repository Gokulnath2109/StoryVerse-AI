from pydantic import BaseModel


class ContinueStoryRequest(BaseModel):
    story_id: str
    choice_id: str