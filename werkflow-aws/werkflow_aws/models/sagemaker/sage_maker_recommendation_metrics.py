from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class SageMakerRecommendationMetrics(BaseModel):
    CostPerHour: StrictFloat | StrictInt | None = None
    CostPerInference: StrictFloat | StrictInt | None = None
    MaxInvocations: StrictInt | None = None
    ModelLatency: StrictInt | None = None
    CpuUtilization: StrictFloat | StrictInt | None = None
    MemoryUtilization: StrictFloat | StrictInt | None = None
    ModelSetupTime: StrictInt | None = None
