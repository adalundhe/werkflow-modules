from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetAdmChannelRequest(BaseModel):
    ApplicationId: StrictStr
