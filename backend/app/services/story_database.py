import json

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.story_db import StoryDB
from app.models.story import Story


def save_story(story: Story):
    db: Session = SessionLocal()

    try:
        existing = db.query(StoryDB).filter(
            StoryDB.story_id == story.story_id
        ).first()

        story_json = json.dumps(story.model_dump())

        if existing:
            existing.story_json = story_json
        else:
            db_story = StoryDB(
                story_id=story.story_id,
                story_json=story_json
            )
            db.add(db_story)

        db.commit()

    finally:
        db.close()


def load_story(story_id: str):
    db: Session = SessionLocal()

    try:
        db_story = db.query(StoryDB).filter(
            StoryDB.story_id == story_id
        ).first()

        if db_story is None:
            return None

        data = json.loads(db_story.story_json)

        return Story(**data)

    finally:
        db.close()