def classify_intent(message: str):
    m = message.lower()

    if "weather" in m:
        return "weather"
    if "search" in m or "report" in m or "find" in m:
        return "semantic"
    if "define" in m or "explain" in m:
        return "concept"
    return "general"
