from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteOptimizationJobRequest(BaseModel):
    OptimizationJobName: StrictStr
