from app.services.gemini_provider import generate_scene as gemini_generate


def generate_scene(story, choice_id):
    return gemini_generate(story, choice_id)