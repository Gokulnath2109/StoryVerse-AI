from fastapi import APIRouter
from app.schemas.story import StoryRequest
from app.services.story_service import generate_story

router = APIRouter()

@router.get("/story")
def get_story():
    return {
        "message": "Story API is working!"
    }

@router.post("/generate-story")
def create_story(request: StoryRequest):
    story = generate_story(
        request.title,
        request.genre,
        request.style,
        request.length
    )

    return {
        "status": "success",
        "story": story
    }