from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeInferenceRouterRequest(BaseModel):
    InferenceRouterName: StrictStr
