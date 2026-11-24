from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerPutEndpointPolicyRequest(BaseModel):
    EndpointName: StrictStr
    ResourcePolicy: StrictStr
