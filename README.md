
# Microsoft Agent Framework – Learning & Experiments

## Overview

This repository is a hands-on exploration of the Microsoft Agent Framework, focusing on building intelligent agents with Azure OpenAI, tool/MCP integration, and real-time streaming. The project demonstrates:

- **Agent Workflow**: Chaining and orchestrating multiple agents for complex tasks.
- **MCP (Model Context Protocol) Integration**: Extending agent capabilities with external tools (e.g., DuckDuckGo web search via Docker).
- **Agent Streaming**: Handling and displaying streaming responses, including tool calls and results, in real time.

---

## Project Structure

- `code/simple_agent.py`: Basic agent using Azure OpenAI.
- `code/simple_agent_with_tools.py`: Agent with tool integration (e.g., weather lookup).
- `code/simple_agent_with_tools_stream.py`: Agent with streaming and function call/result handling.
- `code/simple_agent_HIL.py`: Human-in-the-Loop (HIL) agent requiring user approval for actions.
- `code/agent_with_tool_structured_response.py`: Agent with structured (Pydantic model) LLM responses.
- `code/agent_workflow.py`: Multi-agent workflow, chaining agents and visualizing the workflow.
- `code/agent_mcp_workflow.py`: DuckDuckGo MCP web search agent using Azure OpenAI and MCP tool (via Docker), with streaming output.
- `pyproject.toml`: Project configuration and dependencies.
- `README.md`: This document.

---

## Quick Start

1. **Set up Azure OpenAI** and obtain your endpoint, API key, deployment name, and version.
2. **Set environment variables**:
	 - `azure_endpoint`
	 - `azure_apikey`
	 - `azure_deployment`
	 - `azure_version`
3. **Run an agent example:**
	 ```bash
	 uv run python code/simple_agent.py
	 ```

---

## Highlighted Examples

### 1. Agent Workflow (`code/agent_workflow.py`)

Demonstrates chaining multiple agents together using a workflow. Useful for building complex, multi-step AI solutions. Output can be visualized as an SVG diagram in the `docs/` folder.

### 2. MCP Integration (`code/agent_mcp_workflow.py`)

Shows how to extend agent capabilities with an external tool using MCP. The DuckDuckGo MCP tool runs via Docker, allowing the agent to perform real-time web searches. Example usage:

```bash
uv run python code/agent_mcp_workflow.py
```

### 3. Agent Streaming (`code/simple_agent_with_tools_stream.py`)

Illustrates how to handle and display streaming responses from the agent, including function/tool calls and results, in real time. This is essential for interactive applications and monitoring agent reasoning step by step.

---

## How to Run Other Examples

- **Agent with tool support (e.g., weather lookup):**
	```bash
	uv run python code/simple_agent_with_tools.py
	```
- **Agent with streaming and function call handling:**
	```bash
	uv run python code/simple_agent_with_tools_stream.py
	```
- **Human-in-the-Loop (HIL) agent:**
	```bash
	uv run python code/simple_agent_HIL.py
	```
- **Agent with structured response (Pydantic model output):**
	```bash
	uv run python code/agent_with_tool_structured_response.py
	```
- **Multi-agent workflow example:**
	```bash
	uv run python code/agent_workflow.py
	```

---

## Key Learnings

- How to authenticate and connect to Azure OpenAI.
- Structuring agent instructions and responses.
- Using environment variables for secure configuration.
- Integrating external tools/MCP for enhanced agent capabilities.
- Streaming agent responses and handling tool calls/results in real time.
- Building and visualizing agent workflows.

---

## Next Steps

- Experiment with more complex agent behaviors and tool integrations.
- Integrate with other Azure services.
- Share progress and tips on LinkedIn.

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

