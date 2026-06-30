import uuid

from app.schemas.story import StoryRequest

from app.models.story import Story
from app.models.chapter import Chapter
from app.models.scene import Scene
from app.models.choice import Choice
from app.models.character import Character


def build_story(request: StoryRequest) -> Story:

    # Create Characters
    if request.character_mode.lower() == "custom" and request.characters:
        hero = Character(
            name=request.characters[0],
            role="Hero",
            personality="Brave and curious",
            appearance="To be decided",
            abilities=[],
            background="The hero's journey has just begun."
        )
    else:
        hero = Character(
            name="Unknown Hero",
            role="Hero",
            personality="Brave and curious",
            appearance="To be decided",
            abilities=[],
            background="The hero's journey has just begun."
        )

    # Create Choices
    choice1 = Choice(
        id="explore",
        text="Explore the mysterious forest"
    )

    choice2 = Choice(
        id="village",
        text="Return to the nearby village"
    )

    # Create Scene 1
    scene1 = Scene(
        scene_number=1,
        content="You wake up in a mysterious land. A dark forest lies ahead while a peaceful village can be seen behind you.",
        choices=[choice1, choice2]
    )

    # Create Chapter 1
    chapter1 = Chapter(
        chapter_number=1,
        title="The Beginning",
        scenes=[scene1]
    )

    # Create Story
    story = Story(
        story_id=str(uuid.uuid4()),
        title=request.title,
        genres=request.genres,
        total_chapters=request.chapters,
        characters=[hero],
        chapters=[chapter1],
        current_chapter=1,
        current_scene=1,
        choice_history=[],
        status="ongoing",
        ending=""
    )

    return story