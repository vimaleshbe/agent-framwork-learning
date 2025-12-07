
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

