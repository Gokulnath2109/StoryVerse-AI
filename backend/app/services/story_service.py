import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_story(title: str, genre: str, style: str, length: str):
    prompt = f"""
    Write a {length} {genre} story.

    Title: {title}
    Style: {style}

    Make it engaging, creative, and suitable for interactive storytelling.
    """

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    return response.output_text