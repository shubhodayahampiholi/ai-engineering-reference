import os

import mlflow

from ai_engineering_reference.config import (
    DATABRICKS_HOST,
    DATABRICKS_TOKEN,
    MLFLOW_EXPERIMENT_ID,
    MLFLOW_TRACKING_URI,
)


def configure_tracking() -> None:
    """Configure MLflow for Databricks."""

    os.environ["DATABRICKS_HOST"] = DATABRICKS_HOST
    os.environ["DATABRICKS_TOKEN"] = DATABRICKS_TOKEN

    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment(experiment_id=MLFLOW_EXPERIMENT_ID)