# agent.py
"""
Agent configuration module.
This module sets up the LLM agent, including its model, instructions, and available tools (MCP toolset).
"""
import os
from pathlib import Path
import tools
from google.adk.agents import LlmAgent
from constants import MODEL_NAME

# Initialize the BigQuery MCP toolset
mcp_toolset = tools.get_bigquery_mcp_toolset()

# Create the root agent with the specified model and instructions
root_agent = LlmAgent(
    model=MODEL_NAME,
    name="bigquery_ca_agent",
    instruction=(
        "Help the user answer questions by strategically combining insights from following source: \n"
        "**BigQuery toolset:** access tables from ADKPractice bigquery dataset, understand their schema, and run SQL queries to get relevant data. \n\n"
        "do not use any other datasets\n\n"
    ),
    tools=[mcp_toolset],
)
