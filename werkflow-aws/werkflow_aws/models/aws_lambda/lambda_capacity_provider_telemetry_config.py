from __future__ import annotations
from pydantic import BaseModel
from .lambda_capacity_provider_logging_config import LambdaCapacityProviderLoggingConfig


class LambdaCapacityProviderTelemetryConfig(BaseModel):
    LoggingConfig: LambdaCapacityProviderLoggingConfig | None = None
