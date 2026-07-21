def get_danger_warning(danger_level: int) -> str | None:
    """
    Returns a warning message based on the player's hidden danger level.
    Returns None when no warning should be shown.
    """

    if danger_level < 30:
        return None

    elif danger_level < 60:
        return (
            "Your recent decisions have attracted unwanted attention. "
            "You may be heading toward a risky path."
        )

    elif danger_level < 90:
        return (
            "Your journey is becoming increasingly dangerous. "
            "Future decisions may have serious consequences."
        )

    elif danger_level < 100:
        return (
            "You are approaching a point of no return. "
            "Choose your next actions carefully."
        )

    return (
        "The path you followed has finally led to disaster."
    )