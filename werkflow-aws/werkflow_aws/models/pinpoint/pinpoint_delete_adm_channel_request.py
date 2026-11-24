from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteAdmChannelRequest(BaseModel):
    ApplicationId: StrictStr
