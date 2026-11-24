from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmDeleteRemoteAccessSessionRequest(BaseModel):
    arn: StrictStr
