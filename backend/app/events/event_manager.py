from app.events.event_registry import get_event


class EventManager:

    def start_event(self, story):
        """
        Creates and initializes the correct event.
        """

        if story.active_event is None:
            return

        event_type = story.active_event["type"]

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

        self.current_event = None