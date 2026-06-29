from fastapi import APIRouter

from app.schemas.story import StoryRequest
from app.services.story_service import generate_story
from app.services.story_builder import build_story

router = APIRouter()

@router.get("/story")
def get_story():
    return {
        "message": "Story API is working!"
    }

@router.post("/generate-story")
def create_story(request: StoryRequest):
    story = build_story(request)

    return {
    "status": "success",
    "story": story.model_dump()
    }