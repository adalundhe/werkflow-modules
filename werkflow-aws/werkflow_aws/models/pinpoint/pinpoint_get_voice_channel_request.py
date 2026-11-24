from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetVoiceChannelRequest(BaseModel):
    ApplicationId: StrictStr
