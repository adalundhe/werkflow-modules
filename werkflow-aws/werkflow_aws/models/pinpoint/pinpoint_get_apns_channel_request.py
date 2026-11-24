from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetApnsChannelRequest(BaseModel):
    ApplicationId: StrictStr
