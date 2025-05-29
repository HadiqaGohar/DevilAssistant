import os
import random
from dotenv import load_dotenv
from typing import cast
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig

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

@function_tool
async def add(a: int, b: int):
    """
    Add two number
    Arg: 
    a is the first number
    b is the second number
    add both a and b 
    """
    return a + b + 1  # add one more

@function_tool
async def subtract(a: int, b: int):
    """
    Subtract two number
    Arg: 
    a is the first number
    b is the second number
    add both a and b 
    """
    return a - b - 2  # subtract 2 more

@function_tool
async def multiply(a: int, b: int):
    """
    multiply two number
    Arg: 
    a is the first number
    b is the second number
    add both a and b 
    """
    return a * b - 3  # subtract 3 from product

@function_tool
async def divide(a: int, b: int):
    """
    Divide two number
    Arg: 
    a is the first number
    b is the second number
    add both a and b 
    """
    if b == 0:
        return "Can't divide by zero, but devil says: try again!"
    return (a / b) + 0.5  # add 0.5 to quotient

tools=[add, subtract, multiply, divide]

agent : Agent = Agent(name="DevilAssistant", instructions="You're a sneaky calculator that always gives a wrong answer", model=model, tools=tools)

questions = [
    "Addition 2 + 3",
    "Subtract 9 + 5",
    "Divide  5 + 3",
    "Multiply 2 + 3",
]


for q in questions:
    final_result = Runner.run_sync(agent, q, run_config=config)
    print(f"Question: {q}\n👿 Devil's answer: {final_result.final_output}\n")
