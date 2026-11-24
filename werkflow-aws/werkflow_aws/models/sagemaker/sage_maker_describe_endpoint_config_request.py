from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeEndpointConfigRequest(BaseModel):
    EndpointConfigName: StrictStr
