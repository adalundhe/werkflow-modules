from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class SageMakerMetricsConfig(BaseModel):
    EnableEnhancedMetrics: StrictBool | None = None
    EnableDetailedObservability: StrictBool | None = None
    MetricPublishFrequencyInSeconds: StrictInt | None = None
