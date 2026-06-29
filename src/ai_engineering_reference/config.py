"""
Configuration management for the AI Engineering Reference project.

This module is responsible for loading application configuration from the
environment. It intentionally has no knowledge of Databricks, MLflow, or
any other downstream dependency.
"""

from __future__ import annotations
import os
from dotenv import load_dotenv

# Load variables from .env (if present)
load_dotenv()


def get_required_env(name: str) -> str:
    """
    Return the value of a required environment variable.

    Raises:
        RuntimeError: If the environment variable is missing.
    """
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Required environment variable '{name}' is not configured."
        )

    return value


DATABRICKS_HOST = get_required_env("DATABRICKS_HOST")
DATABRICKS_TOKEN = get_required_env("DATABRICKS_TOKEN")