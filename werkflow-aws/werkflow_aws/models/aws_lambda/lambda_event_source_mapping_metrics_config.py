from __future__ import annotations
from pydantic import BaseModel
from .lambda_event_source_mapping_metric import LambdaEventSourceMappingMetric


class LambdaEventSourceMappingMetricsConfig(BaseModel):
    Metrics: list[LambdaEventSourceMappingMetric] | None = None
