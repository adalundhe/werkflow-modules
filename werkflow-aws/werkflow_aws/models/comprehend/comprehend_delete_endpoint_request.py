from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDeleteEndpointRequest(BaseModel):
    EndpointArn: StrictStr
