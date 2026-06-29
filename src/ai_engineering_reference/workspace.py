"""
Databricks workspace client.
"""

from databricks.sdk import WorkspaceClient

from ai_engineering_reference.config import (
    DATABRICKS_HOST,
    DATABRICKS_TOKEN,
)


def get_workspace_client() -> WorkspaceClient:
    """
    Create an authenticated Databricks Workspace client.
    """
    return WorkspaceClient(
        host=DATABRICKS_HOST,
        token=DATABRICKS_TOKEN,
    )