from abc import ABC, abstractmethod


class BaseEvent(ABC):

    @abstractmethod
    def initialize(self, story):
        """Initialize the event."""
        pass

    @abstractmethod
    def process_action(self, story, action):
        """Handle a player action."""
        pass

    @abstractmethod
    def is_completed(self):
        """Return True when the event has finished."""
        pass

    @abstractmethod
    def get_result(self):
        """Return the event result."""
        pass