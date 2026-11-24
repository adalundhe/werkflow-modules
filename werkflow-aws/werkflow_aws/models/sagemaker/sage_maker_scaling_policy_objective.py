from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerScalingPolicyObjective(BaseModel):
    MinInvocationsPerMinute: StrictInt | None = None
    MaxInvocationsPerMinute: StrictInt | None = None
