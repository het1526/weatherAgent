from langgraph.graph import (
    StateGraph,
    END 
) 
from state import AgentState
from langgraph.prebuilt import ToolNode

from nodes import (
    agent
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

    if last_message.tool_calls:
        return "tools"

    return END

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

builder.set_entry_point(
    "agent"
)

builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        END: END
    }
)

builder.add_edge(
    "tools",
    "agent"
)

graph = builder.compile()