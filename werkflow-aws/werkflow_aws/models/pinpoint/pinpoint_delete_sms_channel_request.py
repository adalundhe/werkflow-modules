from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteSmsChannelRequest(BaseModel):
    ApplicationId: StrictStr
