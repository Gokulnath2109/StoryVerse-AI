import os

from dotenv import load_dotenv
from google import genai
import json

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
  ]
}}

Rules:
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