from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteApnsSandboxChannelRequest(BaseModel):
    ApplicationId: StrictStr
