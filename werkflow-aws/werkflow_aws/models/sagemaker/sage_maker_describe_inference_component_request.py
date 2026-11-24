from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeInferenceComponentRequest(BaseModel):
    InferenceComponentName: StrictStr
