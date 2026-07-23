from app.events.base_event import BaseEvent
from app.events.event_registry import register_event


class ConflictEvent(BaseEvent):

    def __init__(self):
        self.enemy = None
        self.completed = False
        self.result = None

    def initialize(self, story):
        """
        Initialize the conflict event using the data stored
        in story.active_event.
        """
        event_data = story.active_event["data"]
        self.enemy = event_data["enemy"]

        self.completed = False
        self.result = None

    def process_action(self, story, action):
        """
        Prototype conflict system.
        Currently only supports a simple attack action.
        """

        if action != "attack":
            return

        self.enemy["health"] -= 10

        if self.enemy["health"] <= 0:
            self.enemy["health"] = 0
            self.completed = True

            self.result = {
                "summary": f"You overcame {self.enemy['name']}.",
                "game_state_updates": {
                    "experience_change": self.enemy.get("xp_reward", 0),
                    "gold_change": self.enemy.get("gold_reward", 0)
                }
            }

    def is_completed(self):
        return self.completed

    def get_result(self):
        return self.result


register_event("conflict", ConflictEvent)