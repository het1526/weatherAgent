# Weather Agent

A simple AI-powered weather assistant built using **LangGraph**, **LangChain**, **Ollama**, and the **OpenWeatherMap API**.

This project demonstrates the fundamentals of **Agentic AI** by allowing a language model to decide when to use an external tool (weather API) and when to answer directly.

---

## Features

- Natural language weather queries
- Tool calling using LangChain Tools
- Agent workflow built with LangGraph
- Local LLM using Ollama (Llama 3.2)
- Weather data from OpenWeatherMap API
- Guardrails to prevent invalid tool usage
- Fallback responses for non-weather queries

### Example Queries

```text
What's the weather in Mumbai?
```

```text
Tell me the forecast for Delhi.
```

```text
Tell me a science fact.
```

```text
Give me an interesting wildlife fact.
```

---

## Tech Stack

- Python
- LangGraph
- LangChain
- Ollama
- Llama 3.2
- OpenWeatherMap API
- Requests
- Python Dotenv

---

## Project Structure

```text
weather-agent/
│
├── app.py
├── graph.py
├── nodes.py
├── state.py
├── tools.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Agent Workflow

```text
User Query
      │
      ▼
    Agent
      │
      ▼
Tool Required?
 ┌────┴────┐
 │         │
Yes        No
 │         │
 ▼         ▼
Weather   Direct
 Tool     Response
 │
 ▼
Agent
 │
 ▼
Response
```

### Weather Query Example

```text
User:
What's the weather in Mumbai?
```

Agent decides:

```text
Call weather tool
```

Tool executes:

```text
get_weather("Mumbai")
```

Weather API returns data.

Agent generates a final response for the user.

---

## Installation

### 1. Clone Repository

```bash
git clone <your-repository-url>
cd weather-agent
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Ollama Setup

Install Ollama:

https://ollama.com

Pull the model:

```bash
ollama pull llama3.2
```

Verify:

```bash
ollama run llama3.2
```

---

## OpenWeatherMap Setup

Create a free account:

https://openweathermap.org/api

Generate an API key.

---

## Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
WEATHER_API_KEY=your_openweathermap_api_key
```

---

## Running the Application

```bash
python app.py
```

Example:

```text
Ask something: What's the weather in Mumbai?
```

Output:

```text
The temperature in Mumbai is 31°C with scattered clouds.
```

---

## Concepts Demonstrated

- Agentic AI fundamentals
- Tool calling
- LangGraph workflows
- State management
- Conditional routing
- Guardrails
- Fallback handling
- External API integration

---

## Future Improvements

- Multi-tool support
- Weather forecast support
- Location validation
- Structured outputs
- Memory and conversation history
- Multiple LLM providers
- Streamlit web interface
- Voice interaction

---

## Learning Objective

This project was built as a hands-on introduction to Agentic AI systems and LangGraph-based workflows, serving as a foundation for more advanced agents involving document processing, PDF comparison, and automation workflows.
