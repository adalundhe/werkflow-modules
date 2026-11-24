from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmGetProjectRequest(BaseModel):
    arn: StrictStr
