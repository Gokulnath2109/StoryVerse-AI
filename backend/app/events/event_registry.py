EVENT_REGISTRY = {}


def register_event(name: str, event_class):
    EVENT_REGISTRY[name] = event_class


def get_event(name: str):
    return EVENT_REGISTRY.get(name)