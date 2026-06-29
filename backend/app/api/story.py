from fastapi import APIRouter

from app.schemas.story import StoryRequest
from app.schemas.continue_story import ContinueStoryRequest
from app.services.story_builder import build_story
from app.services.story_store import story_store

router = APIRouter()


@router.post("/generate-story")
def create_story(request: StoryRequest):
    story = build_story(request)
    story_store[story.story_id] = story

    return {
        "status": "success",
        "story": story.model_dump()
    }

@router.post("/continue-story")
def continue_story(request: ContinueStoryRequest):

    story = story_store.get(request.story_id)

    if story is None:
        return {
            "status": "error",
            "message": "Story not found."
        }

    return {
        "status": "success",
        "story": story.model_dump(),
        "selected_choice": request.choice_id
    }

