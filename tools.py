from langchain_core.tools import tool
import requests
import os


@tool
def get_weather(city: str):
    """
    Get current weather for a city.

    Use ONLY when the user explicitly asks
    about weather, temperature, rain,
    forecast, climate, humidity,
    or atmospheric conditions.

    Do NOT use for general knowledge,
    jokes, wildlife facts, history,
    programming, or unrelated questions.
    """

    api_key = os.getenv("WEATHER_API_KEY")

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={api_key}"
        "&units=metric"
    )

    response = requests.get(url)

    return response.json()