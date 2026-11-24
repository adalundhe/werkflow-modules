from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerScalingPolicyMetric(BaseModel):
    InvocationsPerInstance: StrictInt | None = None
    ModelLatency: StrictInt | None = None
