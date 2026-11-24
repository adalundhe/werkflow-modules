from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetApnsVoipChannelRequest(BaseModel):
    ApplicationId: StrictStr
