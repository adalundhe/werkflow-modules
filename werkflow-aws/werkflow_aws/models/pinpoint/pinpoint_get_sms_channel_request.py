from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetSmsChannelRequest(BaseModel):
    ApplicationId: StrictStr
