from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmGetInstanceProfileRequest(BaseModel):
    arn: StrictStr
