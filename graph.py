from langgraph.graph import (
    StateGraph,
    END 
) 
from state import AgentState
from langgraph.prebuilt import ToolNode

from nodes import (
    agent,
    fallback_chat
)

from tools import(
    get_weather
)

tool_node = ToolNode(
    [get_weather]
)

def should_continue(state):

    messages = state["messages"]

    last_message = messages[-1]

    if not last_message.tool_calls:
        return END

    tool_call = last_message.tool_calls[0]

    user_query = messages[0].content.lower()

    weather_keywords = [
        "weather",
        "temperature",
        "forecast",
        "rain",
        "humidity",
        "climate",
        "hot",
        "cold"
    ]

    if any(
        word in user_query
        for word in weather_keywords
    ):
        return "tools"

    print("Blocked invalid tool call")

    return "fallback"

builder = StateGraph(
    AgentState
)

builder.add_node(
    "agent",
    agent
)

builder.add_node(
    "tools",
    tool_node
)

builder.add_node(
    "fallback",
    fallback_chat
)

builder.set_entry_point(
    "agent"
)

builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "fallback": "fallback",
        END: END
    }
)

builder.add_edge(
    "tools",
    "agent"
)

builder.add_edge(
    "fallback",
    END
)

graph = builder.compile()