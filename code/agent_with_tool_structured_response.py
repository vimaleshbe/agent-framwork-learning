
import os
import asyncio
from agent_framework.azure import AzureOpenAIChatClient
from typing import Annotated
from pydantic import Field,BaseModel

###########################################################
# Agent Configuration Constants
# These define the agent's name and instructions.
###########################################################
AGENT_NAME = "Indian-Agent"
AGENT_INSTRUCTIONS = (
    "You are a helpful assistant that figures out the city from the information provided and also returns weather."
)



# Structured response model for the LLM
class CityInfo(BaseModel):
    name: str | None = None  # City name
    weather: str | None = None  # Weather description



def get_weather(location: Annotated[str, Field(description="The location to get weather for")]) -> str:
    """
    Tool function to get weather information for a given location.
    In a real implementation, this would call a weather API.
    """
    # Placeholder response for demonstration
    return f"The weather in {location} is rainy for the next 2 days."




async def simple_agent_with_tools():
    """
    Main function to run the agent with tool support and print a structured response to a sample query.
    Demonstrates how to get a structured (Pydantic model) response from the LLM.
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

    # Run a sample query and print the structured result
    # The response will be parsed into the CityInfo model
    response = await agent.run("I am at the Marina beach.", response_format=CityInfo)
    print(response)

# Entry point: run the agent for structured response demonstration
if __name__ == "__main__":
    asyncio.run(simple_agent_with_tools())

if __name__ == "__main__":
    # Entry point: run the agent with tools asynchronously
    asyncio.run(simple_agent_with_tools())