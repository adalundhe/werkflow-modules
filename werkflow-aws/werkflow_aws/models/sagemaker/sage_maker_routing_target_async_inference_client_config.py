from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerRoutingTargetAsyncInferenceClientConfig(BaseModel):
    MaxTimeInBacklogSeconds: StrictInt | None = None
