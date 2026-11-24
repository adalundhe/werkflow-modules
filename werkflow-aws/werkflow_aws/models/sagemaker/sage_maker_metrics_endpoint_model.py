from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerMetricsEndpointModel(BaseModel):
    MetricsEndpointPath: StrictStr | None = None
    MetricPublishFrequencyInSeconds: StrictInt | None = None
