from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmGetSuiteRequest(BaseModel):
    arn: StrictStr
