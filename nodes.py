from tools import get_weather
from langchain_ollama import ChatOllama

tools = [get_weather]

llm = ChatOllama(
    model="llama3.2"
)

llm_with_tools = llm.bind_tools(tools)

def agent(state):

    messages = state["messages"]

    response = llm_with_tools.invoke(messages)

    print("Tool Calls:")
    print(response.tool_calls)
    
    return {
        "messages": [response]
    }

