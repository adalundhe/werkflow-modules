from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStopProcessingJobRequest(BaseModel):
    ProcessingJobName: StrictStr
