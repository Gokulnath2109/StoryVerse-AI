import uuid

from app.models.story import Story
from app.models.chapter import Chapter
from app.schemas.story import StoryRequest


def build_story(request: StoryRequest) -> Story:

    first_chapter = Chapter(
        chapter_number=1,
        title="The Beginning",
        content="This is the beginning of your adventure.",
        choices=[]
    )

    return Story(
        story_id=str(uuid.uuid4()),
        title=request.title,
        genre=request.genre,
        style=request.style,
        length=request.length,
        chapters=[first_chapter]
    )