from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmDeleteNetworkProfileRequest(BaseModel):
    arn: StrictStr
