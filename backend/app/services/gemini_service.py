import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_scene(story, choice_id):
    """
    Temporary Gemini integration.
    Later we'll replace the prompt with the full StoryVerse prompt.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Say hello in one sentence."
    )

    return {
        "content": response.text,
        "choices": [
            {
                "id": "choice1",
                "text": "Continue"
            },
            {
                "id": "choice2",
                "text": "Stop"
            },
            {
                "id": "choice3",
                "text": "Look Around"
            },
            {
                "id": "choice4",
                "text": "Run"
            }
        ]
    }