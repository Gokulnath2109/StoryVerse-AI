from sqlalchemy import Column, String, Text

from app.database import Base


class StoryDB(Base):
    __tablename__ = "stories"

    story_id = Column(String, primary_key=True, index=True)
    story_json = Column(Text, nullable=False)