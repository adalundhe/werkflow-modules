from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerClusterOperationScalingConfiguration(BaseModel):
    CurrentCount: StrictInt | None = None
    TargetCount: StrictInt | None = None
    MinCount: StrictInt | None = None
