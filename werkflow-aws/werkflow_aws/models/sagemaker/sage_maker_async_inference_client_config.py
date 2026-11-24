from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerAsyncInferenceClientConfig(BaseModel):
    MaxConcurrentInvocationsPerInstance: StrictInt | None = None
