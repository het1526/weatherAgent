from dotenv import load_dotenv

load_dotenv()

from graph import graph

query = input(
    "Ask something: "
)

result = graph.invoke(
    {
        "messages": [
            (
                "user",
                query
            )
        ]
    }
)

print(
    result["messages"][-1].content
)

