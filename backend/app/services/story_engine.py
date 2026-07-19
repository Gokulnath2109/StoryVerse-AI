from app.models.story import Story
from app.models.scene import Scene
from app.models.choice import Choice
from app.services.gemini_service import generate_scene


def continue_story(story: Story, choice_id: str) -> Story:
    """
    Continues the story using the Gemini service.
    """

    # Save player's choice
    story.choice_history.append(choice_id)

    # Move to next scene
    story.current_scene += 1

    # Ask Gemini Service (currently returns placeholder data)
    response = generate_scene(story, choice_id)

    # Convert JSON response into Scene object
    scene = Scene(
        scene_number=story.current_scene,
        content=response["content"],
        choices=[
            Choice(
                id=choice["id"],
                text=choice["text"]
            )
            for choice in response["choices"]
        ]
    )

    # Add scene to current chapter
    story.chapters[story.current_chapter - 1].scenes.append(scene)

    return story