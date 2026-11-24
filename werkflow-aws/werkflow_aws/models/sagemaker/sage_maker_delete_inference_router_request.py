from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteInferenceRouterRequest(BaseModel):
    InferenceRouterName: StrictStr
