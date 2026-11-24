from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteApnsVoipChannelRequest(BaseModel):
    ApplicationId: StrictStr
