from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteEndpointRequest(BaseModel):
    ApplicationId: StrictStr
    EndpointId: StrictStr
