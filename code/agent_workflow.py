
import os
import asyncio
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework import AgentExecutor, AgentRunUpdateEvent, WorkflowBuilder, WorkflowOutputEvent, WorkflowStatusEvent, WorkflowViz
from typing import Annotated
from pydantic import Field,BaseModel



# Structured response model for the LLM
class CityInfo(BaseModel):
    name: str | None = None  # City name
    weather: str | None = None  # Weather description




# Tool function for weather lookup
def get_weather(location: Annotated[str, Field(description="The location to get weather for")]) -> str:
    """
    Tool function to get weather information for a given location.
    In a real implementation, this would call a weather API.
    """
    # Placeholder response for demonstration
    return f"The weather in {location} is sunny for the next 2 days."





async def simple_agent_with_tools():
    """
    Main function to run a multi-agent workflow with tool support and print structured responses.
    Demonstrates how to chain agents using a workflow and visualize the process.
    """
    # Load Azure OpenAI configuration from environment variables
    endpoint = os.getenv("azure_endpoint")
    api_key = os.getenv("azure_apikey")
    deployment_name = os.getenv("azure_deployment")
    api_version = os.getenv("azure_version")

    # Validate required environment variables
    if not all([endpoint, api_key, deployment_name, api_version]):
        raise EnvironmentError("Missing one or more required Azure OpenAI environment variables.")

    try:
        # Create the first agent: Indian Weather Agent
        indian_weather_agent = AgentExecutor(AzureOpenAIChatClient(
            endpoint=endpoint,
            deployment_name=deployment_name,
            api_version=api_version,
            api_key=api_key
        ).create_agent(
            name="Indian-Weather-Agent",
            instructions="You are IWA, a helpful assistant that figures out the city from the information provided and also returns weather.",
            tools=get_weather,
            response_format=CityInfo
        ))

        # Create the second agent: Indian Tourist Agent
        indian_tourist_agent = AgentExecutor(AzureOpenAIChatClient(
            endpoint=endpoint,
            deployment_name=deployment_name,
            api_version=api_version,
            api_key=api_key
        ).create_agent(
            name="Indian-Tourist-Agent",
            instructions=(
                "You are ITA, an assistant who provides tourist recommendations based on a city. "
                "Your input might be a JSON object that includes 'city' or 'weather'. "
                "Base your response on 'city' and 'weather'. If the weather is sunny and warm, recommend an outdoor place. "
                "Else recommend an indoor place. Do not recommend the place you are already at. "
                "Return JSON with a single field response."
            )
        ))

        # Build the workflow: weather agent feeds into tourist agent
        workflow = WorkflowBuilder().set_start_executor(indian_weather_agent).add_edge(indian_weather_agent, indian_tourist_agent).build()

        # Visualize the workflow and save as SVG
        viz = WorkflowViz(workflow)
        doc_diagram = viz.save_svg("docs/agent_workflow.svg")

        # Run the workflow with a sample input and stream events
        events = workflow.run_stream("I am currently at Marina Beach")

        last_executor_id: str | None = None

        async for event in events:
            if isinstance(event, AgentRunUpdateEvent):
                eid = event.executor_id
                if eid != last_executor_id:
                    if last_executor_id is not None:
                        print()
                    print(f"{eid}:", end=" ", flush=True)
                    last_executor_id = eid
                print(event.data, end="", flush=True)
            elif isinstance(event, WorkflowStatusEvent):
                print("\n=== Status ===")
                print(event)

    finally:
        pass



# Entry point: run the agent workflow demonstration
if __name__ == "__main__":
    asyncio.run(simple_agent_with_tools())