from app.events.base_event import BaseEvent


class CombatEvent(BaseEvent):

    def __init__(self):
        self.enemy_name = ""
        self.enemy_health = 0
        self.enemy_max_health = 0

        self.completed = False
        self.result = None

    def initialize(self, story, event_data):
        self.enemy = event_data["enemy"]
        self.completed = False
        self.result = None

    def process_action(self, story, action):
        if action != "attack":
            return

        self.enemy["health"] -= 10

        if self.enemy["health"] <= 0:
            self.enemy["health"] = 0
            self.completed = True

            self.result = {
            "summary": f"You defeated {self.enemy['name']}.",
            "game_state_updates": {
                "experience_change": self.enemy.get("xp_reward", 0),
                "gold_change": self.enemy.get("gold_reward", 0)
            }
        }

    def is_completed(self):
        return self.completed

    def get_result(self):
        return self.result