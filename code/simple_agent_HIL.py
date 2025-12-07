
import os
import asyncio
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework import ChatMessage,Role, ai_function, TextContent, FunctionCallContent, FunctionResultContent,FunctionApprovalRequestContent
from typing import Annotated
from pydantic import Field

###########################################################
# Agent Configuration Constants
# These define the agent's name and instructions.
###########################################################
AGENT_NAME = "Indian-Agent"
AGENT_INSTRUCTIONS = (
    "You are my Indian Agent, you know all about India. "
    "You can answer questions and use tools to provide information."
)



# This tool function requires human approval before execution (Human-in-the-Loop)
@ai_function(approval_mode="always_require")
def get_weather(location: Annotated[str, Field(description="The location to get weather for")]) -> str:
    """
    Tool function to get weather information for a given location.
    In a real implementation, this would call a weather API.
    """
    # Placeholder response for demonstration
    return f"The weather in {location} is rainy for the next 2 days."



async def hil_example():
    """
    Main function to run the agent with Human-in-the-Loop (HIL) tool support and stream the response to a sample query.
    Demonstrates how human approval is required before executing certain functions.
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

    # Stream agent responses and handle different content types
    async for update in agent.run_stream("What is the weather in Chennai?"):
        for content in update.contents:
            # Print text content from the agent
            if isinstance(content, TextContent):
                print(f"[TextContent] {content.text}")
            # Print function call details
            elif isinstance(content, FunctionCallContent):
                print(f"[FunctionCallContent] Name: {content.name}")
                print(f"Arguments: {content.arguments}")
                print(f"Call ID: {content.call_id}")
            # Print function result
            elif isinstance(content, FunctionResultContent):
                print(f"[FunctionResultContent] {content.result}")
            # Print approval request details (Human-in-the-Loop)
            elif isinstance(content, FunctionApprovalRequestContent):
                print(f"[FunctionApprovalRequestContent] call : {content.function_call.call_id}")
                print(f"[FunctionApprovalRequestContent] args : {content.function_call.arguments}")

    # If the agent requests user input for approval, handle it here
    if update.user_input_requests:
        for user_input_need in update.user_input_requests:
            print(f"Function : {user_input_need.function_call.name}")
            print(f"args : {user_input_need.function_call.arguments}")

        # Simulate user approval (Human-in-the-Loop)
        user_approval = True
        approval_message = ChatMessage(role=Role.USER, contents=[user_input_need.create_response(user_approval)])

        # Run the agent with the approval message and print the final result
        final_result = await agent.run([
            "what is the current weather in chennai ?",
            ChatMessage(role=Role.ASSISTANT, contents=[user_input_need]),
            approval_message
        ])
        print(final_result)





# Entry point: run the agent with Human-in-the-Loop tool and stream response asynchronously
if __name__ == "__main__":
    asyncio.run(hil_example())