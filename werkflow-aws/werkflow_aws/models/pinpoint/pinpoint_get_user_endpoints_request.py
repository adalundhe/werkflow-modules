from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetUserEndpointsRequest(BaseModel):
    ApplicationId: StrictStr
    UserId: StrictStr
