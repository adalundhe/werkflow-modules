from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeAIBenchmarkJobRequest(BaseModel):
    AIBenchmarkJobName: StrictStr
