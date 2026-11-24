from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerInferenceMetrics(BaseModel):
    MaxInvocations: StrictInt | None = None
    ModelLatency: StrictInt | None = None
