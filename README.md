
# Microsoft Agent Framework Learning Journey

## Author

This project is maintained by Vimalesh Jeyavelmani.

## Overview

This repository documents my exploration and learning of the **Microsoft Agent Framework**. My goal is to understand how to build intelligent agents using Azure OpenAI and share my experience through LinkedIn and other platforms.

## What is Microsoft Agent Framework?

Microsoft Agent Framework is a toolkit for building AI-powered agents that can interact with users, automate tasks, and integrate with Azure services. It leverages Azure OpenAI for natural language understanding and generation.

## My Learning Goals

- Understand the basics of agent-based architectures.
- Learn how to configure and use Azure OpenAI within the framework.
- Build a simple agent that can answer questions about India.
- Document the process and share insights for others starting out.






## Project Structure

- `code/simple_agent.py`: Basic agent implementation using Azure OpenAI.
- `code/simple_agent_with_tools.py`: Agent implementation with tool integration (e.g., weather lookup).
- `code/simple_agent_with_tools_stream.py`: Agent implementation demonstrating streaming responses and function call handling.
- `code/simple_agent_HIL.py`: Human-in-the-Loop (HIL) agent implementation, requiring user approval for certain actions.
- `code/agent_with_tool_structured_response.py`: Agent implementation that demonstrates structured (Pydantic model) responses from the LLM.
- `code/agent_workflow.py`: Multi-agent workflow example, chaining agents and visualizing the workflow.
- `code/agent_mcp_workflow.py`: DuckDuckGo MCP web search agent example using Azure OpenAI and an MCP tool (DuckDuckGo via Docker).
- `pyproject.toml`: Project configuration and dependencies.
- `README.md`: This document.


## How to Run

1. Set up Azure OpenAI and obtain your endpoint, API key, deployment name, and version.
2. Set the following environment variables:
	- `azure_endpoint`
	- `azure_apikey`
	- `azure_deployment`
	- `azure_version`
3. Run a sample agent:
	```bash
	uv run python code/simple_agent.py
	```

4. To try the agent with tool support (e.g., weather lookup):
	```bash
	uv run python code/simple_agent_with_tools.py
	```

5. To try the agent with streaming responses and function call handling:
	```bash
	uv run python code/simple_agent_with_tools_stream.py
	```

6. To try the Human-in-the-Loop (HIL) agent:
	```bash
	uv run python code/simple_agent_HIL.py
	```

7. To try the agent with structured response (Pydantic model output):
	```bash
	uv run python code/agent_with_tool_structured_response.py
	```
8. To try the multi-agent workflow example:
	```bash
	uv run python code/agent_workflow.py
	```

9. To try the DuckDuckGo MCP web search agent example:
	```bash
	uv run python code/agent_mcp_workflow.py
	```

	This example demonstrates how to use an agent with Azure OpenAI and an MCP tool (DuckDuckGo web search via Docker) to answer queries. The agent streams the final result to the console.
## Agent Workflow Example

The `agent_workflow.py` example demonstrates how to chain multiple agents together using a workflow. The output can be visualized as an SVG diagram in the `docs/` folder. This is useful for building more complex, multi-step AI solutions.
## Structured LLM Responses

The `agent_with_tool_structured_response.py` example demonstrates how to instruct the LLM to return structured data (using a Pydantic model) instead of plain text. This is useful for downstream automation, validation, and integration with other systems.
## What is Human-in-the-Loop (HIL)?

Human-in-the-Loop (HIL) is a design pattern where certain actions performed by an AI agent require explicit approval or input from a human user before proceeding. This is useful for scenarios where oversight, safety, or compliance is important. In this project, the HIL agent demonstrates how to require user approval before executing a tool function.



## Key Learnings

- How to authenticate and connect to Azure OpenAI.
- Structuring agent instructions and responses.
- Using environment variables for secure configuration.
- Writing clean, maintainable Python code.
- Integrating external tools/functions with agents for enhanced capabilities.
- Streaming agent responses and handling function calls/results in real time.

## Next Steps

- Experiment with more complex agent behaviors and tool integrations.
- Integrate with other Azure services.
- Share my progress and tips on LinkedIn.

