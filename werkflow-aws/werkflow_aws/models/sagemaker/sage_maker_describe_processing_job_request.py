from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeProcessingJobRequest(BaseModel):
    ProcessingJobName: StrictStr
