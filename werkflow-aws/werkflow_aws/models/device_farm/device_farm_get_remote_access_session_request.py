from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmGetRemoteAccessSessionRequest(BaseModel):
    arn: StrictStr
