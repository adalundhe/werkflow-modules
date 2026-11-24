from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteEndpointRequest(BaseModel):
    EndpointName: StrictStr
