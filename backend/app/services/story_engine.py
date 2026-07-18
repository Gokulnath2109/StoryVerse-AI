from app.models.story import Story
from app.models.scene import Scene
from app.models.choice import Choice


def continue_story(story: Story, choice_id: str) -> Story:

    # Save user's choice
    story.choice_history.append(choice_id)

    # Move to next scene
    story.current_scene += 1

    # Create placeholder Scene 2
    scene = Scene(
        scene_number=story.current_scene,
        content=f"This is Scene {story.current_scene}. You selected '{choice_id}'.",
        choices=[
            Choice(
                id="continue",
                text="Continue forward"
            ),
            Choice(
                id="return",
                text="Go back"
            )
        ]
    )

    # Add scene to current chapter
    story.chapters[story.current_chapter - 1].scenes.append(scene)

    return story