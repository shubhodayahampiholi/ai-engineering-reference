from contextlib import contextmanager

import mlflow


@contextmanager
def trace(
    application: str,
    business_capability: str,
    environment: str,
    market: str,
    user_id: str,
):
    with mlflow.start_span(name="business_request") as span:
        span.set_attribute("application", application)
        span.set_attribute("business_capability", business_capability)
        span.set_attribute("environment", environment)
        span.set_attribute("market", market)
        span.set_attribute("user_id", user_id)

        yield span