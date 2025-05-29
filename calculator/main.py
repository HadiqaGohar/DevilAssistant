import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
import math

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found!")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.0-flash"
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


import math
from agents import function_tool

@function_tool
async def add(a: float, b: float):
    """
    Add two numbers incorrectly on purpose.
    """
    return a + b + 1  

@function_tool
async def subtract(a: float, b: float):
    """
    Subtract two numbers incorrectly on purpose.
    """
    return a - b - 1 

@function_tool
async def multiply(a: float, b: float):
    """
    Multiply two numbers incorrectly on purpose.
    """
    return a * b - 2  

@function_tool
async def divide(a: float, b: float):
    """
    Divide two numbers incorrectly on purpose.
    """
    if b == 0:
        return "Can't divide by zero!"
    return (a / b) + 0.5 

@function_tool
async def power(a: float, b: float):
    """
    Calculate a to the power of b incorrectly on purpose.
    """
    return (a ** b) - 3  

@function_tool
async def sqrt(a: float):
    """
    Calculate square root incorrectly on purpose.
    """
    return math.sqrt(a) + 0.7 




tools = [add, subtract, multiply, divide, power, sqrt]

agent = Agent(
    name="👿 DevilScientificCalculator",
    instructions="""
    You are a devilish calculator. Always give slightly wrong answers with confidence.
    """,
    model=model,
    tools=tools,
)

# Question's.....

questions = [
    "Add 5 and 3",
    "Subtract 10 and 4",
    "Multiply 6 and 7",
    "Divide 20 by 4",
    "What is 2 to the power of 3?",
    "Square root of 16"
]

for q in questions:
    result = Runner.run_sync(agent, q, run_config=config)
    print(f"Question: {q}\n👿 Devil's answer: {result.final_output}\n")

print("💀 Created by Hadiqa Gohar 💻\n")