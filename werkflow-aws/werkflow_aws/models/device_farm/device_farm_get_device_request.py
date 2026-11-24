from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmGetDeviceRequest(BaseModel):
    arn: StrictStr
