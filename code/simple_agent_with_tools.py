
import os
import asyncio
from agent_framework.azure import AzureOpenAIChatClient
from typing import Annotated
from pydantic import Field

# =============================
# Agent Configuration Constants
# =============================
AGENT_NAME = "Indian-Agent"
AGENT_INSTRUCTIONS = (
    "You are my Indian Agent, you know all about India. "
    "You can answer questions and use tools to provide information."
)


def get_weather(location: Annotated[str, Field(description="The location to get weather for")]) -> str:
    """
    Tool function to get weather information for a given location.
    In a real implementation, this would call a weather API.
    """
    # Placeholder response for demonstration
    return f"The weather in {location} is rainy for the next 2 days."



async def simple_agent_with_tools():
    """
    Main function to run the agent with tool support and print the response to a sample query.
    """
    # Load Azure OpenAI configuration from environment variables
    endpoint = os.getenv("azure_endpoint")
    api_key = os.getenv("azure_apikey")
    deployment_name = os.getenv("azure_deployment")
    api_version = os.getenv("azure_version")

    # Validate required environment variables
    if not all([endpoint, api_key, deployment_name, api_version]):
        raise EnvironmentError("Missing one or more required Azure OpenAI environment variables.")

    # Create the agent with specified name, instructions, and tool(s)
    agent = AzureOpenAIChatClient(
        endpoint=endpoint,
        deployment_name=deployment_name,
        api_version=api_version,
        api_key=api_key
    ).create_agent(
        name=AGENT_NAME,
        instructions=AGENT_INSTRUCTIONS,
        tools=get_weather
    )

    # Run a sample query and print the result
    response = await agent.run("What is the weather in Chennai?")
    print(response)


if __name__ == "__main__":
    # Entry point: run the agent with tools asynchronously
    asyncio.run(simple_agent_with_tools())