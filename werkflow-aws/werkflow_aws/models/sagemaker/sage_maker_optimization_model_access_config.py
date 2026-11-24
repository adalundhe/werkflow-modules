from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SageMakerOptimizationModelAccessConfig(BaseModel):
    AcceptEula: StrictBool | None = None
