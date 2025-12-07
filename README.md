# Microsoft Agent Framework Learning Journey

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

- `code/simple_agent.py`: My first agent implementation using Azure OpenAI.
- `pyproject.toml`: Project configuration and dependencies.
- `README.md`: This document.

## How to Run

1. Set up Azure OpenAI and obtain your endpoint, API key, deployment name, and version.
2. Set the following environment variables:
	- `azure_endpoint`
	- `azure_apikey`
	- `azure_deployment`
	- `azure_version`
3. Run the agent:
	```bash
	python code/simple_agent.py
	```

## Key Learnings

- How to authenticate and connect to Azure OpenAI.
- Structuring agent instructions and responses.
- Using environment variables for secure configuration.
- Writing clean, maintainable Python code.

