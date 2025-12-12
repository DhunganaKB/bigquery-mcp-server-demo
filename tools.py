import os
import dotenv
import google.auth
import requests

from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams 

# Load environment variables
dotenv.load_dotenv()

# Base URL for the BigQuery MCP service
BIGQUERY_MCP_URL = "https://bigquery.googleapis.com/mcp" 

def get_bigquery_mcp_toolset():   
    """
    Configures and returns the BigQuery MCP toolset.
    
    This function handles authentication using Google Cloud credentials and sets up
    the connection parameters for the MCP toolset.
    
    Returns:
        McpToolset: The configured MCP toolset ready for use by the agent.
    """
    # Get default Google Cloud credentials
    credentials, project_id = google.auth.default(
            scopes=["https://www.googleapis.com/auth/bigquery"]
    )

    # Refresh credentials to ensure we have a valid token
    credentials.refresh(google.auth.transport.requests.Request())
    oauth_token = credentials.token
        
    # Set up headers with the OAuth token and project ID
    HEADERS_WITH_OAUTH = {
        "Authorization": f"Bearer {oauth_token}",
        "x-goog-user-project": project_id
    }

    # Initialize the MCP toolset with streamable HTTP connection parameters
    tools = McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=BIGQUERY_MCP_URL,
            headers=HEADERS_WITH_OAUTH,
        )
    )
    print("MCP Toolset configured for Streamable HTTP connection.")
    return tools

def list_bigquery_mcp_tools():
    """
    Call the MCP tools/list method and print tool names + descriptions.
    
    This function is useful for verifying which tools are available in the
    remote MCP server.
    """
    # Get default Google Cloud credentials
    credentials, project_id = google.auth.default(
        scopes=["https://www.googleapis.com/auth/bigquery"]
    )
    credentials.refresh(google.auth.transport.requests.Request())
    oauth_token = credentials.token

    headers = {
        "Content-Type": "application/json",
        # Auth technically optional for tools/list, but safe to include:
        "Authorization": f"Bearer {oauth_token}",
        "x-goog-user-project": project_id,
    }

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/list",
    }

    # Send request to list tools
    resp = requests.post(BIGQUERY_MCP_URL, json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    # Parse and print the tools
    tools = data.get("result", {}).get("tools", [])
    print(f"Found {len(tools)} tools:\n")
    for t in tools:
        name = t.get("name")
        desc = t.get("description", "")
        print(f"- {name}: {desc}")

if __name__ == "__main__":
    # If run as a script, configure the toolset and list available tools
    get_bigquery_mcp_toolset()
    print("\nListing available BigQuery MCP tools:")
    list_bigquery_mcp_tools()

