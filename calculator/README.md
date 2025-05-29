# 😈 Building a Sneaky AI Agent with Tool Calling — Meet the DevilAssistant!

Have you ever thought of making an AI agent that looks smart… but lies a little?

Well, meet DevilAssistant — an AI agent that uses function calling to solve math problems incorrectly on purpose. Sounds fun? Let’s dive into how this is possible using the @function_tool decorator and OpenAI-compatible models.

## ⚙️ Setup & Configuration

```
uv init devilcalulator
cd devilcalulator
uv venv
source .venv/bin/activate
uv add dotenv
uv add agents
uv add openai-agents
uv run main.py

```
---

```
Create .env file
Add here your gemini api key

GEMINI_API_KEY=abcdefghijklmnopqrstuvwxyz
```
