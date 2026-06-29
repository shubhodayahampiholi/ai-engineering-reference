import mlflow

from ai_engineering_reference.mlflow.tracking import configure_tracking
from ai_engineering_reference.telemetry.tracing import trace

configure_tracking()


@mlflow.trace
def generate_response(question: str) -> str:
    return f"Response for: {question}"


if __name__ == "__main__":

    with trace(
        application="ai-engineering-reference",
        business_capability="Sales Insights",
        environment="dev",
        market="Germany",
        user_id="shubhodaya",
    ):
        response = generate_response(
            "What are the sales trends for Sensodyne in Germany?"
        )

        print(response)