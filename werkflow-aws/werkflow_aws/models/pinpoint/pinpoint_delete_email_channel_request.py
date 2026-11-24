from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteEmailChannelRequest(BaseModel):
    ApplicationId: StrictStr
