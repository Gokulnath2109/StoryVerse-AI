from app.models.story import Story
from app.models.scene import Scene
from app.models.choice import Choice
from app.models.chapter import Chapter
from app.events.event_manager import EventManager
from app.services.ai_manager import generate_scene
from app.services.danger_manager import get_danger_warning

MAX_SCENES_PER_CHAPTER = 5

event_manager = EventManager()

def continue_story(story: Story, choice_id: str) -> Story:
    """
    Continues the story using Gemini and updates the player's game state.
    """

    # Save player's choice
    story.choice_history.append(choice_id)

    # --------------------------------------------------
    # Generate next scene from Gemini
    # --------------------------------------------------

    response = generate_scene(story, choice_id)

    if response.get("event") is not None:
        story.active_event = response["event"]
        event_manager.start_event(story)
    else:
        story.active_event = None

    # --------------------------------------------------
    # Update Game State
    # --------------------------------------------------

    updates = response.get("game_state_updates", {})

    story.game_state.health += updates.get("health_change", 0)
    story.game_state.mana += updates.get("mana_change", 0)
    story.game_state.gold += updates.get("gold_change", 0)
    story.game_state.experience += updates.get("experience_change", 0)

    # Danger System
    danger_change = updates.get("danger_change", 0)

    story.game_state.danger_level += danger_change

    # Keep danger between 0 and 100
    story.game_state.danger_level = max(
        0,
        min(100, story.game_state.danger_level)
    )

    if story.game_state.danger_level >= 100:

        story.status = "ended"

        story.ending = (
            "The danger you ignored has reached its peak. "
            "The world has fallen into darkness."
        )

        return story

    story.game_state.health = max(0, story.game_state.health)
    story.game_state.mana = max(0, story.game_state.mana)
    story.game_state.gold = max(0, story.game_state.gold)
    story.game_state.experience = max(0, story.game_state.experience)

    # Inventory
    for item in updates.get("add_inventory", []):
        if item not in story.game_state.inventory:
            story.game_state.inventory.append(item)

    for item in updates.get("remove_inventory", []):
        if item in story.game_state.inventory:
            story.game_state.inventory.remove(item)

    # Quests
    for quest in updates.get("add_quests", []):
        if quest not in story.game_state.quests:
            story.game_state.quests.append(quest)

    for quest in updates.get("remove_quests", []):
        if quest in story.game_state.quests:
            story.game_state.quests.remove(quest)

    # ----------------------------
    # Update Relationships
    # ----------------------------

    for npc, change in updates.get("relationship_updates", {}).items():
        if npc not in story.game_state.relationships:
            story.game_state.relationships[npc] = 0

        story.game_state.relationships[npc] += change

    # --------------------------------------------------
    # Chapter Progression
    # --------------------------------------------------

    current_chapter = story.chapters[story.current_chapter - 1]

    if len(current_chapter.scenes) >= MAX_SCENES_PER_CHAPTER:

        # Create next chapter only if available
        if story.current_chapter < story.total_chapters:

            story.current_chapter += 1
            story.current_scene = 1

            new_chapter = Chapter(
                chapter_number=story.current_chapter,
                title=f"Chapter {story.current_chapter}",
                scenes=[]
            )

            story.chapters.append(new_chapter)

            current_chapter = new_chapter

        else:
            # Stay in last chapter
            story.current_scene += 1

    else:
        story.current_scene += 1

    # --------------------------------------------------
    # Create Scene
    # --------------------------------------------------

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

    current_chapter.scenes.append(scene)

    warning = get_danger_warning(story.game_state.danger_level)

    if warning:
        story.warning_message = warning
    else:
        story.warning_message = None

    return story