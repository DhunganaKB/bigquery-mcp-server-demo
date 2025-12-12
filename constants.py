# constants.py
"""
Configuration constants for the application.
This module contains project-specific settings, including Google Cloud configuration,
agent settings, and the list of BigQuery tables to be used.
"""

# GCP + BigQuery config
# Replace with your actual Google Cloud Project ID
PROJECT_ID = "project-id"
# Replace with your BigQuery dataset location (e.g., "us-central1", "global")
LOCATION = "us-central1"

# ADK / Agent config
APP_NAME = "bigquery_conversational_app_remote"
MODEL_NAME = "gemini-2.0-flash"

# Fixed list of tables for your app (edit this only)
# Each element is a dict with dataset + table
# These tables are exposed to the agent for querying
TABLES = [
    {
        "dataset": "dataset-id",
        "table": "table-id",
    },
    {
        "dataset": "dataset-id",
        "table": "table-id",
    },
    # add more here:
    # {"dataset": "other_dataset", "table": "other_table"},
]
