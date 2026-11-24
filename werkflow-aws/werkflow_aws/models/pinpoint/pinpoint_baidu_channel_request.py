from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class PinpointBaiduChannelRequest(BaseModel):
    ApiKey: StrictStr
    SecretKey: StrictStr
    Enabled: StrictBool | None = None
