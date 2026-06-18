from dotenv import load_dotenv

load_dotenv()

from graph import graph

query = input(
    "Ask about weather: "
)

result = graph.invoke(
    {
        "user_query": query
    }
)

print(
    result["response"]
)

