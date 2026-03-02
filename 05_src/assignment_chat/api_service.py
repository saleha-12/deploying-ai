import requests

def get_weather(city: str):
    """
    Fetches weather information for a given city using the free Open-Meteo API.
    Returns a clean, human-readable description.
    """

    # Step 1 — Geocoding: convert city name to coordinates
    geo = requests.get(
        f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    ).json()

    if "results" not in geo:
        return f"Sorry, I couldn't find weather information for '{city}'."

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    # Step 2 — Get weather data
    weather = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    ).json()

    current = weather.get("current_weather", {})

    temperature = current.get("temperature", "unknown")
    windspeed = current.get("windspeed", "unknown")

    # Step 3 — Return natural-language answer
    return (
        f"In {city}, the temperature is {temperature}°C "
        f"with winds around {windspeed} km/h."
    )
