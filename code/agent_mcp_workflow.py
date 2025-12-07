

# =========================================
# DuckDuckGo MCP Web Search Agent Example
# =========================================
# This script demonstrates how to use an agent with Azure OpenAI and an MCP tool
# (DuckDuckGo web search via Docker) to answer queries, streaming the final result.
#
# Author: <Your Name>
# Date: 2025-12-07
# =========================================

import os
import asyncio
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework import ChatAgent, MCPStdioTool

async def agent_mcp_duckduckgo():
    """Example using DuckDuckGo MCP server via Docker for web search.
    
    This function sets up the DuckDuckGo MCP tool and the Azure OpenAI chat agent,
    allowing for web searches to be performed and results to be printed.
    """
    
    # Load Azure OpenAI configuration from environment variables
    endpoint = os.getenv("azure_endpoint")
    api_key = os.getenv("azure_apikey")
    deployment_name = os.getenv("azure_deployment")
    api_version = os.getenv("azure_version")

    # Validate required environment variables
    if not all([endpoint, api_key, deployment_name, api_version]):
        raise EnvironmentError("Missing one or more required Azure OpenAI environment variables.")

    # Create the DuckDuckGo MCP tool (runs via Docker)
    async with (
        MCPStdioTool(
            name="duckduckgo",
            command="docker",
            args=[
                "run",
                "-i",
                "duckduckgo-mcp-server:latest"
            ]
        ) as ddg_tool,
        # Create the chat agent with Azure OpenAI
        ChatAgent(
            chat_client=AzureOpenAIChatClient(
                endpoint=endpoint,
                deployment_name=deployment_name,
                api_version=api_version,
                api_key=api_key
            ),
            name="WebSearchAgent",
            instructions="You are a helpful assistant that can answer questions by searching the web using DuckDuckGo.",
        ) as agent,
    ):
        # Define the query to run
        query = "What is the capital of France?"
        # Stream the agent's response and print only the final result
        async for event in agent.run_stream(query, tools=ddg_tool):
            contents = getattr(event, 'contents', [])
            for content in contents:
                if hasattr(content, "text"):
                    print(content.text, end="", flush=True)




# Entry point: run the DuckDuckGo MCP agent
if __name__ == "__main__":
    asyncio.run(agent_mcp_duckduckgo())