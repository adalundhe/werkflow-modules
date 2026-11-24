from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeEndpointRequest(BaseModel):
    EndpointName: StrictStr
