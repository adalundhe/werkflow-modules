from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetBaiduChannelRequest(BaseModel):
    ApplicationId: StrictStr
