from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_metrics_endpoint import SageMakerMetricsEndpoint


class SageMakerContainerMetricsConfig(BaseModel):
    MetricsEndpoints: list[SageMakerMetricsEndpoint] | None = None
