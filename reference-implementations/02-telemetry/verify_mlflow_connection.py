import mlflow

from ai_engineering_reference.mlflow.tracking import configure_tracking

configure_tracking()

print("=" * 80)
print("MLflow Version")
print("=" * 80)
print(mlflow.__version__)

print()

print("=" * 80)
print("Tracking URI")
print("=" * 80)
print(mlflow.get_tracking_uri())