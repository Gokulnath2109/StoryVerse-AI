import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def build_prompt(story, choice_id):

    previous_story = ""

    for chapter in story.chapters:
        for scene in chapter.scenes:
            previous_story += f"Scene {scene.scene_number}: {scene.content}\n\n"

    prompt = f"""
You are an expert interactive storyteller.

Rules:
- Continue the story naturally.
- Never repeat previous scenes.
- Never contradict previous events.
- Stay within the given genres.
- Give exactly 4 meaningful choices.
- Do not end the story unless instructed.
- Return ONLY valid JSON.
- Never return markdown.
- Never explain your answer.

Story Title:
{story.title}

Genres:
{", ".join(story.genres)}

Main Character:
{story.characters[0].name}

Current Chapter:
{story.current_chapter}

Choice History:
{story.choice_history}

Latest Choice:
{choice_id}

Previous Story:
{previous_story}

Game State:

Health: {story.game_state.health}
Mana: {story.game_state.mana}
Level: {story.game_state.level}
Experience: {story.game_state.experience}
Gold: {story.game_state.gold}

Inventory:
{", ".join(story.game_state.inventory) if story.game_state.inventory else "Empty"}

Quests:
{", ".join(story.game_state.quests) if story.game_state.quests else "None"}

Companions:
{", ".join(story.game_state.companions) if story.game_state.companions else "None"}

Relationships:
{story.game_state.relationships}

Generate the next scene.

Return ONLY valid JSON.

The JSON must follow this format exactly:

{{
  "content": "Next scene description",

  "choices": [
    {{
      "id": "choice_1",
      "text": "First choice"
    }},
    {{
      "id": "choice_2",
      "text": "Second choice"
    }},
    {{
      "id": "choice_3",
      "text": "Third choice"
    }},
    {{
      "id": "choice_4",
      "text": "Fourth choice"
    }}
  ],

  "game_state_updates": {{
    "health_change": 0,
    "mana_change": 0,
    "gold_change": 0,
    "experience_change": 0,
    "danger_change": 0,

    "add_inventory": [],
    "remove_inventory": [],

    "add_quests": [],
    "remove_quests": [],

    "relationship_updates": {{}}
  }}
}}

Game State Rules:

- Use health_change to increase or decrease health.
- Use mana_change to increase or decrease mana.
- Use gold_change to increase or decrease gold.
- Use experience_change to award experience.
- If the player finds an item, put it in add_inventory.
- If the player loses an item, put it in remove_inventory.
- If the player starts a quest, put it in add_quests.
- If the player completes a quest, put it in remove_quests.
- If nothing changes, leave all values as 0 or empty lists.

Relationship Update Rules (MANDATORY)

- After generating the next scene, identify all named NPCs involved in the scene.
- Determine whether the player's latest choice affects each NPC's opinion of the player.
- If a relationship changes, update it in relationship_updates using the NPC's exact name.
- Use positive values for improved relationships and negative values for worsened relationships.
- If multiple NPCs are affected, include all of them.
- Do not invent NPCs that are not part of the story.
- If no relationship changes occur, return an empty object:

"relationship_updates": {{}}

Danger System Rules:

- Analyze the player's latest choice and its consequences.
- Increase danger for reckless, suspicious, harmful, or dangerous choices.
- Decrease danger for safe, helpful, or intelligent choices.
- Use danger_change values between -20 and +30.
- If the choice does not affect danger, return 0.
- Never set danger_change directly to 100.

Final Rules:

- Return ONLY JSON.
- No markdown.
- No explanations.
- No extra text.
- Exactly 4 choices.
- Each choice id must be unique.
"""

    return prompt


def generate_scene(story, choice_id):

    prompt = build_prompt(story, choice_id)

    print("\n" + "=" * 80)
    print("PROMPT SENT TO GEMINI")
    print("=" * 80)
    print(prompt)
    print("=" * 80)

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    print("\n" + "=" * 80)
    print("GEMINI RAW RESPONSE")
    print("=" * 80)
    print(response.text)
    print("=" * 80 + "\n")

    scene = json.loads(response.text)

    return scene