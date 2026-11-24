from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmStopRemoteAccessSessionRequest(BaseModel):
    arn: StrictStr
