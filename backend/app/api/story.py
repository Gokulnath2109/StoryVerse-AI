from fastapi import APIRouter

router = APIRouter()

@router.get("/story")
def get_story():
    return {
        "message": "Story API is working!"
    }