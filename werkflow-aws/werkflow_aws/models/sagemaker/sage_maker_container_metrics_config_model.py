from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_metrics_endpoint_model import SageMakerMetricsEndpointModel


class SageMakerContainerMetricsConfigModel(BaseModel):
    MetricsEndpoints: list[SageMakerMetricsEndpointModel] | None = None
