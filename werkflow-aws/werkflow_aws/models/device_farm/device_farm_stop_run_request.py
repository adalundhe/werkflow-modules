from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmStopRunRequest(BaseModel):
    arn: StrictStr
