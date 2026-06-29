"""
Application configuration.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Required environment variable '{name}' is not configured."
        )

    return value


DATABRICKS_HOST = get_required_env("DATABRICKS_HOST")
DATABRICKS_TOKEN = get_required_env("DATABRICKS_TOKEN")
MLFLOW_TRACKING_URI = get_required_env("MLFLOW_TRACKING_URI")
MLFLOW_EXPERIMENT_ID = get_required_env("MLFLOW_EXPERIMENT_ID")