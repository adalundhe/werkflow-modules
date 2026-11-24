from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmGetDeviceInstanceRequest(BaseModel):
    arn: StrictStr
