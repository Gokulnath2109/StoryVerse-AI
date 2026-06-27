from fastapi import FastAPI
from app.api.story import router as story_router

app = FastAPI()

app.include_router(story_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to StoryVerse AI Backend!"
    }