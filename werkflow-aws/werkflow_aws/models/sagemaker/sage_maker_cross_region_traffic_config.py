from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerCrossRegionTrafficConfig(BaseModel):
    MaxInvocationsPerSecondPerInstance: StrictInt | None = None
    MaxCrossRegionPercentPerEndpoint: StrictInt | None = None
