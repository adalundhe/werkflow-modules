from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetEndpointRequest(BaseModel):
    ApplicationId: StrictStr
    EndpointId: StrictStr
