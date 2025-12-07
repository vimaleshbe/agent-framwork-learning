import os
import asyncio
from agent_framework.azure import AzureOpenAIResponsesClient

# Agent configuration constants
AGENT_NAME = "Indian-Agent"
AGENT_INSTRUCTIONS = "You are my Indian Agent, you know all about India."



async def simpleAgent():
    """
    Main function to run the agent and print the response to a sample query.
    """
    # Load Azure OpenAI configuration from environment variables
    endPoint = os.getenv("azure_endpoint")
    apiKey = os.getenv("azure_apikey")
    deploymentName = os.getenv("azure_deployment")
    version = os.getenv("azure_version")

    # Create the agent with specified name and instructions
    agent = AzureOpenAIResponsesClient(
        endpoint=endPoint,
        deployment_name=deploymentName,
        api_version=version,
        api_key=apiKey
    ).create_agent(
        name=AGENT_NAME,
        instructions=AGENT_INSTRUCTIONS,
    )

    # Run a sample query and print the result
    print(await agent.run("What is the capital of India?"))

if __name__ == "__main__":
    # Run the agent asynchronously
    asyncio.run(simpleAgent())