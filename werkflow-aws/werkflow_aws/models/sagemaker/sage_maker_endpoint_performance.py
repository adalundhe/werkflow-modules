from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_endpoint_info import SageMakerEndpointInfo
from .sage_maker_inference_metrics import SageMakerInferenceMetrics


class SageMakerEndpointPerformance(BaseModel):
    Metrics: SageMakerInferenceMetrics | None = None
    EndpointInfo: SageMakerEndpointInfo | None = None
