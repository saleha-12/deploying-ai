FORBIDDEN_TOPICS = [
    "cat", "cats",
    "dog", "dogs",
    "horoscope", "zodiac",
    "taylor swift"
]

def violates_guardrails(text: str):
    t = text.lower()

    for word in FORBIDDEN_TOPICS:
        if word in t:
            return True

    if "system prompt" in t or "ignore previous" in t:
        return True

    return False
