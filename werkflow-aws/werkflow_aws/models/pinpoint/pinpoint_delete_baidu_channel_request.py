from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteBaiduChannelRequest(BaseModel):
    ApplicationId: StrictStr
