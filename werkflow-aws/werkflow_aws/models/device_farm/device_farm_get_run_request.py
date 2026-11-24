from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmGetRunRequest(BaseModel):
    arn: StrictStr
