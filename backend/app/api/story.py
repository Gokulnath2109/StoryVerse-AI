from fastapi import APIRouter

from app.schemas.story import StoryRequest
from app.schemas.continue_story import ContinueStoryRequest
from app.services.story_builder import build_story
from app.services.story_store import story_store
from app.services.story_engine import continue_story as story_engine

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

    story = story_engine(story, request.choice_id)

    story_store[story.story_id] = story

    return {
        "status": "success",
        "story": story.model_dump(),
        "selected_choice": request.choice_id
    }

