from tools import get_weather
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2"
)

def extract_city(state):

    query = state["user_query"]

    prompt = f"""
    Extract only the city name.

    Query:
    {query}
    """

    city = llm.invoke(prompt)
    print(city.content)

    return {
        "city": city.content.strip()
    }

def fetch_weather(state):

    city = state["city"]

    weather = get_weather(city)

    print(weather)

    return {
        "weather_data": weather
    }

def generate_response(state):

    weather = state["weather_data"]

    if weather.get("cod") != 200:

        return {
            "response":
            f"Could not find weather data. "
            f"Reason: {weather.get('message')}"
        }

    temp = weather["main"]["temp"]

    description = weather["weather"][0]["description"]

    return {
        "response":
        f"The temperature in {state['city']} "
        f"is {temp}°C with {description}."
    }