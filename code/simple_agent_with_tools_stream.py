
import os
import asyncio
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework import TextContent, FunctionCallContent, FunctionResultContent
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


async def simple_agent_with_tools_stream():
    """
    Main function to run the agent with tool support and stream the response to a sample query.
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

    # Run a sample query and stream the result

    print("Streaming response:")
    async for update in agent.run_stream("What is the weather in Chennai?"):
        # Each update may contain multiple content types
        for content in update.contents:
            # Use direct isinstance checks for content types
            if isinstance(content, TextContent):
                print(f"{content.text}", end="", flush=True)
            elif isinstance(content, FunctionCallContent):
                print(f"\n[Function Call] Name: {content.name}", flush=True)
                print(f"Arguments: {content.arguments}", flush=True)
                print(f"Call ID: {content.call_id}", flush=True)
            elif isinstance(content, FunctionResultContent):
                print(f"\n[Function Result] {content.result}\n", flush=True)
            else:
                # Fallback for unknown types
                if getattr(content, "type", None) == "text":
                    print(content.text, end="", flush=True)
                elif getattr(content, "type", None) == "functionCall":
                    print(f"\n[Function Call] {content.name}({content.arguments})\n", flush=True)
                elif getattr(content, "type", None) == "functionResult":
                    print(f"\n[Function Result] {content.result}\n", flush=True)

if __name__ == "__main__":
    # Entry point: run the agent with tools and stream response asynchronously
    asyncio.run(simple_agent_with_tools_stream())