from langgraph.graph import StateGraph
from langgraph.graph import END
from state import AgentState

from nodes import (
    extract_city,
    fetch_weather,
    generate_response,
    router,
    normal_chat
)

builder = StateGraph(AgentState)

def route_decision(state):

    return state["route"]

builder.add_node(
    "extract_city",
    extract_city
)

builder.add_node(
    "fetch_weather",
    fetch_weather
)

builder.add_node(
    "generate_response",
    generate_response
)

builder.add_node(
    "router",
    router
)

builder.add_node(
    "chat",
    normal_chat
)

builder.set_entry_point(
    "router"
)

builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "weather": "extract_city",
        "chat": "chat"
    }
)

builder.add_edge(
    "extract_city",
    "fetch_weather"
)

builder.add_edge(
    "fetch_weather",
    "generate_response"
)

builder.add_edge(
    "chat",
    END
)

builder.add_edge(
    "generate_response",
    END
)


graph = builder.compile()