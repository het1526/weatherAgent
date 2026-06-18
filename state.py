from typing import TypedDict


class AgentState(TypedDict):

    user_query: str

    city: str

    weather_data: dict

    response: str