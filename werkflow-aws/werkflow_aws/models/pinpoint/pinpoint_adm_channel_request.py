from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class PinpointADMChannelRequest(BaseModel):
    ClientId: StrictStr
    ClientSecret: StrictStr
    Enabled: StrictBool | None = None
