from tools import get_weather
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage

tools = [get_weather]

llm = ChatOllama(
    model="llama3.2"
)

system_prompt = SystemMessage(
    content="""
    Get current weather information.

    REQUIRED:
    - A real city name must be provided.

    Examples:
    - Mumbai
    - Delhi
    - London
    - Paris

    Never use:
    - none
    - unknown
    - empty values

    Use only when the user asks about weather,
    temperature, rain, humidity, forecast,
    or climate conditions.
    """
)

llm_with_tools = llm.bind_tools(tools)

def agent(state):

    messages = state["messages"]

    response = llm_with_tools.invoke([system_prompt] + messages)

    # print("Tool Calls:")
    # print(response.tool_calls)

    return {
        "messages": [response]
    }

def fallback_chat(state):

    query = state["messages"][0].content

    response = llm.invoke(query)

    return {
        "messages": [response]
    }