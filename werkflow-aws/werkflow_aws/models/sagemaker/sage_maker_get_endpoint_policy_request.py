from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerGetEndpointPolicyRequest(BaseModel):
    EndpointName: StrictStr
