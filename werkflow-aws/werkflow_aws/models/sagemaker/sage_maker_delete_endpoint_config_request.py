from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteEndpointConfigRequest(BaseModel):
    EndpointConfigName: StrictStr
