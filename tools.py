import requests
import os

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city: str):

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        "&units=metric"
    )

    response = requests.get(url)

    return response.json()