from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmStopJobRequest(BaseModel):
    arn: StrictStr
