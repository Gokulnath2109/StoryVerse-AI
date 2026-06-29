from fastapi import APIRouter

from app.schemas.story import StoryRequest
from app.schemas.continue_story import ContinueStoryRequest
from app.services.story_builder import build_story

router = APIRouter()


@router.post("/generate-story")
def create_story(request: StoryRequest):
    story = build_story(request)

    return {
        "status": "success",
        "story": story.model_dump()
    }


@router.post("/continue-story")
def continue_story(request: ContinueStoryRequest):
    return {
        "status": "success",
        "message": "Continue story endpoint is working.",
        "story_id": request.story_id,
        "choice_id": request.choice_id
    }
