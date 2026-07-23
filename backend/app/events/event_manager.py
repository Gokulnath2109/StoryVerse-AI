from app.events.event_registry import get_event


class EventManager:

    def __init__(self):
        self.current_event = None

    def start_event(self, event_type: str, story):
        event_class = get_event(event_type)

        if event_class is None:
            return

        self.current_event = event_class()
        self.current_event.initialize(story)

    def process_action(self, story, action):

        if self.current_event is None:
            return

        self.current_event.process_action(story, action)

    def is_event_active(self):
        return self.current_event is not None

    def finish_event(self):

        if self.current_event is None:
            return None

        result = self.current_event.get_result()

        self.current_event = None

        return result