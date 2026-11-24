from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetChannelsRequest(BaseModel):
    ApplicationId: StrictStr
