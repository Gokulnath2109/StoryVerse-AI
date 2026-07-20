from fastapi import FastAPI

from app.database import Base, engine
from app.models.story_db import StoryDB

Base.metadata.create_all(bind=engine)

from app.api.story import router as story_router

app = FastAPI()

app.include_router(story_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to StoryVerse AI Backend!"
    }