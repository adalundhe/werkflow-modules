from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeOptimizationJobRequest(BaseModel):
    OptimizationJobName: StrictStr
