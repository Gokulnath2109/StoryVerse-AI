import uuid

from app.models.story import Story
from app.schemas.story import StoryRequest


def build_story(request: StoryRequest) -> Story:
    return Story(
        story_id=str(uuid.uuid4()),
        title=request.title,
        genre=request.genre,
        style=request.style,
        length=request.length
    )