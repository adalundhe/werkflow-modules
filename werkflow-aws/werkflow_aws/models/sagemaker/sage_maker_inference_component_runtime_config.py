from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerInferenceComponentRuntimeConfig(BaseModel):
    CopyCount: StrictInt
