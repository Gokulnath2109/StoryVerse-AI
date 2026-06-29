import uuid

from app.models.story import Story
from app.models.chapter import Chapter
from app.models.character import Character
from app.schemas.story import StoryRequest
from app.models.choice import Choice

def build_story(request: StoryRequest) -> Story:

    hero = Character(
        name="Unknown Hero",
        role="Hero",
        personality="Brave and curious",
        appearance="To be decided",
        abilities=[],
        background="The hero's journey has just begun."
    )

    fight_choice = Choice(
    id="fight",
    text="Fight the dragon",
    next_chapter=2,
    consequence="The dragon becomes angry."
    )

    run_choice = Choice(
    id="run",
    text="Run away",
    next_chapter=2,
    consequence="You escape safely."
    )

    first_chapter = Chapter(
        chapter_number=1,
        title="The Beginning",
        content="This is the beginning of your adventure.",
        choices=[fight_choice,run_choice]
    )

    return Story(
        story_id=str(uuid.uuid4()),
        title=request.title,
        genre=request.genre,
        style=request.style,
        length=request.length,
        characters=[hero],
        chapters=[first_chapter]
    )