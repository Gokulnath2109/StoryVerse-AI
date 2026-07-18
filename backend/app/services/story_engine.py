from app.models.story import Story
from app.models.scene import Scene
from app.models.choice import Choice


def continue_story(story: Story, choice_id: str) -> Story:
    """
    Continues the story based on the player's choice.
    """

    # Save the player's choice
    story.choice_history.append(choice_id)

    # Move to the next scene
    story.current_scene += 1

    # ---------- Branching Story Logic ----------

    if choice_id == "explore":

        scene = Scene(
            scene_number=story.current_scene,
            content=(
                "You enter the dark forest. Strange sounds echo through the trees. "
                "A glowing wolf appears in the distance and silently watches you."
            ),
            choices=[
                Choice(
                    id="follow_wolf",
                    text="Follow the glowing wolf"
                ),
                Choice(
                    id="hide",
                    text="Hide behind a tree"
                )
            ]
        )

    elif choice_id == "village":

        scene = Scene(
            scene_number=story.current_scene,
            content=(
                "You return to the peaceful village. The villagers welcome you warmly. "
                "An old man approaches and asks for your help."
            ),
            choices=[
                Choice(
                    id="help_old_man",
                    text="Help the old man"
                ),
                Choice(
                    id="visit_market",
                    text="Visit the village market"
                )
            ]
        )

    elif choice_id == "follow_wolf":

        scene = Scene(
            scene_number=story.current_scene,
            content=(
                "The glowing wolf leads you to ancient ruins hidden deep inside the forest. "
                "A mysterious stone door stands before you."
            ),
            choices=[
                Choice(
                    id="open_door",
                    text="Open the stone door"
                ),
                Choice(
                    id="go_back",
                    text="Go back"
                )
            ]
        )

    elif choice_id == "hide":

        scene = Scene(
            scene_number=story.current_scene,
            content=(
                "You hide behind a large tree. The wolf disappears, but you notice a strange map "
                "lying on the ground."
            ),
            choices=[
                Choice(
                    id="take_map",
                    text="Take the mysterious map"
                ),
                Choice(
                    id="ignore_map",
                    text="Ignore it and continue walking"
                )
            ]
        )

    elif choice_id == "help_old_man":

        scene = Scene(
            scene_number=story.current_scene,
            content=(
                "The old man tells you about a legendary crystal hidden beneath the village temple."
            ),
            choices=[
                Choice(
                    id="visit_temple",
                    text="Visit the temple"
                ),
                Choice(
                    id="ask_more",
                    text="Ask for more information"
                )
            ]
        )

    elif choice_id == "visit_market":

        scene = Scene(
            scene_number=story.current_scene,
            content=(
                "The village market is crowded. A mysterious merchant offers you an ancient sword."
            ),
            choices=[
                Choice(
                    id="buy_sword",
                    text="Buy the sword"
                ),
                Choice(
                    id="leave_market",
                    text="Leave the market"
                )
            ]
        )

    else:

        scene = Scene(
            scene_number=story.current_scene,
            content="Your journey continues into the unknown...",
            choices=[
                Choice(
                    id="continue",
                    text="Continue"
                )
            ]
        )

    # Add the newly created scene to the current chapter
    story.chapters[story.current_chapter - 1].scenes.append(scene)

    return story