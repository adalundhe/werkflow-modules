from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeEdgePackagingJobRequest(BaseModel):
    EdgePackagingJobName: StrictStr
