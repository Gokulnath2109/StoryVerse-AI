from app.services import gemini_provider
from app.services import groq_provider


def generate_scene(story, choice_id):
    """
    Generate the next scene using Gemini.
    If Gemini fails (quota, network, API error, etc.),
    automatically switch to Groq.
    """

    try:
        print("\nUsing Gemini...\n")
        return gemini_provider.generate_scene(story, choice_id)

    except Exception as e:
        print("\n" + "=" * 80)
        print("Gemini failed.")
        print(e)
        print("Switching to Groq...")
        print("=" * 80 + "\n")

        try:
            return groq_provider.generate_scene(story, choice_id)

        except Exception as groq_error:
            print("\n" + "=" * 80)
            print("Groq also failed.")
            print(groq_error)
            print("=" * 80 + "\n")
            raise Exception("All AI providers are currently unavailable.")