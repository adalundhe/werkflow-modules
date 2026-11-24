from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteUserEndpointsRequest(BaseModel):
    ApplicationId: StrictStr
    UserId: StrictStr
