from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteAIBenchmarkJobRequest(BaseModel):
    AIBenchmarkJobName: StrictStr
