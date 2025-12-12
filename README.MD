# Remote BigQuery MCP Server

This project implements a remote Model Context Protocol (MCP) server for BigQuery, enabling interaction with BigQuery datasets using Google's Generative AI models.

## Remote BigQuery MCP Set Up

To run this, you need to set up  Google Cloud CLI `gcloud` from the terminal and enable some services.

### Prerequisites & Service Enablement

1.  **Authenticate with Google Cloud**:
    ```bash
    gcloud config set project `<your-project-id>`
    gcloud auth application-default login
    ```

2.  **Set Project ID**:
    In your terminal, set your project ID variable:
    ```bash
    PROJECT_ID=<your-project-id>
    ```

3.  **Enable Required Services**:
    Run the following commands to enable Vertex AI, API Keys, and the BigQuery MCP service:
    ```bash
    gcloud services enable aiplatform.googleapis.com --project=$PROJECT_ID
    gcloud services enable apikeys.googleapis.com --project=$PROJECT_ID
    gcloud beta services mcp enable bigquery.googleapis.com --project=$PROJECT_ID
    ```

### Environment Configuration

Create a `.env` file in the root of this directory with the following content:

For Vertex AI Run:

```env
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=<your-project-id>
GOOGLE_CLOUD_LOCATION=global
```

For Gemini Developer API Run:

```env
GOOGLE_API_KEY=<your-api-key>
```

### Verification

1.  **Check if MCP is Enabled**:
    Verify that the BigQuery MCP service is enabled for your project:
    ```bash
    PROJECT_ID=$(gcloud config get-value project)
    gcloud beta services mcp list --enabled --project="$PROJECT_ID" \
      --format="value(name)"
    ```

    If it is not enabled, run:
    ```bash
    gcloud beta services mcp enable bigquery.googleapis.com --project="$PROJECT_ID"
    ```

2.  **Test Connection**:
    You can verify the connection to the MCP server using `curl`.
    
    First, verify the URL is correct:
    `BIGQUERY_MCP_URL = "https://bigquery.googleapis.com/mcp"`

    Then, run the following command:
    ```bash
    ACCESS_TOKEN=$(gcloud auth print-access-token)

    curl -i \
      -H "Authorization: Bearer $ACCESS_TOKEN" \
      -H "x-goog-user-project: $PROJECT_ID" \
      -H "Content-Type: application/json" \
      https://bigquery.googleapis.com/mcp
    ```

## Reference

For more detailed steps and information, please refer to the original Google MCP repository:
[https://github.com/google/mcp.git](https://github.com/google/mcp.git)
