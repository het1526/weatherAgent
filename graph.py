from langgraph.graph import StateGraph

from state import AgentState

from nodes import (
    extract_city,
    fetch_weather,
    generate_response
)

builder = StateGraph(AgentState)

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

builder.set_entry_point(
    "extract_city"
)

builder.add_edge(
    "extract_city",
    "fetch_weather"
)

builder.add_edge(
    "fetch_weather",
    "generate_response"
)

graph = builder.compile()