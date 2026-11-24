from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStopTransformJobRequest(BaseModel):
    TransformJobName: StrictStr
