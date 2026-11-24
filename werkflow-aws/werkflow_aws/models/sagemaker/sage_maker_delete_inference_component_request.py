from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteInferenceComponentRequest(BaseModel):
    InferenceComponentName: StrictStr
