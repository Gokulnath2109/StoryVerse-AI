# 📖 StoryVerse AI

StoryVerse AI is an AI-powered interactive RPG storytelling platform where every player's decision shapes a unique adventure.

Unlike traditional fixed stories, StoryVerse AI dynamically generates scenes, choices, and game updates based on player actions, creating a personalized storytelling experience.

---

# ✨ Features

## 🤖 AI-Powered Story Generation
- Dynamic story creation using Large Language Models.
- AI-generated scenes and meaningful choices.
- Story continuation based on previous decisions.

## 🎮 Interactive Choice System
- Players control the direction of the story.
- Every choice affects future scenes and game progression.

## 🎯 RPG Game State Management
The system tracks:

- ❤️ Health
- 🔮 Mana
- ⭐ Experience
- 🏆 Gold
- 🎒 Inventory
- 📜 Quests
- 🤝 Relationships

## 🤝 NPC Relationship System
- Tracks player interactions with characters.
- Relationships can increase or decrease based on decisions.

Example:

```json
{
  "Eira": 9
}
```

## 💾 Persistent Story Storage
- SQLite database integration.
- Stories are saved permanently.
- Player progress remains available after server restart.

## 🔄 Multi AI Provider Support
Supports multiple AI providers:

- Google Gemini
- Groq (Llama)

Automatic fallback:

```
Gemini
   |
   | (failure/quota limit)
   ↓
Groq
```

## 🚀 FastAPI Backend
- REST API architecture.
- Automatic Swagger documentation.
- Modular service-based design.

---

# 🛠️ Tech Stack

## Backend

- Python 3.11
- FastAPI
- Uvicorn

## AI

- Google Gemini API
- Groq API (Llama 3.3 70B)

## Database

- SQLite
- SQLAlchemy

## Validation

- Pydantic

## Tools

- Git
- GitHub

---

# 📂 Project Structure

```
StoryVerse AI
│
└── backend
    │
    ├── app
    │   │
    │   ├── api
    │   │   └── story.py
    │   │
    │   ├── services
    │   │   ├── story_builder.py
    │   │   ├── story_engine.py
    │   │   ├── gemini_provider.py
    │   │   ├── groq_provider.py
    │   │   └── story_database.py
    │   │
    │   ├── models
    │   │   └── story_db.py
    │   │
    │   ├── schemas
    │   │
    │   ├── database.py
    │   └── main.py
    │
    ├── storyverse.db
    ├── requirements.txt
    └── README.md
```

---

# 🔌 API Endpoints

## Generate Story

```
POST /generate-story
```

Creates a new interactive story.

---

## Continue Story

```
POST /continue-story
```

Continues the story based on the player's selected choice.

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 📌 Version 1.0.0

## Completed Features

✅ AI story generation  
✅ Dynamic scene generation  
✅ Interactive choices  
✅ Chapter and scene management  
✅ Game state system  
✅ Inventory system  
✅ Quest system  
✅ NPC relationships  
✅ SQLite persistence  
✅ Gemini integration  
✅ Groq integration  
✅ Automatic AI fallback  
✅ Git version control  

---

# 🗺️ Future Roadmap

## Version 2

Planned features:

- ⚔️ Combat System
- 👹 Enemy System
- 🪄 Skills and Abilities
- 🛡️ Equipment System
- 👥 Companion System
- 🗺️ World Map
- 📜 Advanced Quest System
- 🧠 Improved AI Memory

---

# 🏗️ Architecture

```
Player
  |
  ↓
FastAPI Backend
  |
  ↓
AI Manager
  |
  ├── Gemini
  |
  └── Groq
  |
  ↓
Story Engine
  |
  ↓
Game State Update
  |
  ↓
SQLite Database
```

---

# 👨‍💻 Author

**Gokulnath S**

AI & ML Student  
Backend Developer | AI Enthusiast

GitHub:
https://github.com/Gokulnath2109

---

# 📜 License

This project is developed for learning and portfolio purposes.
