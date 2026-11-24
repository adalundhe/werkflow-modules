from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmGetUploadRequest(BaseModel):
    arn: StrictStr
