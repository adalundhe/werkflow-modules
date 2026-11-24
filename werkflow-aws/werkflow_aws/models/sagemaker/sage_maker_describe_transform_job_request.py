from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeTransformJobRequest(BaseModel):
    TransformJobName: StrictStr
