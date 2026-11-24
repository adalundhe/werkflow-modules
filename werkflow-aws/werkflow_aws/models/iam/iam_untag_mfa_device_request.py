from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUntagMFADeviceRequest(BaseModel):
    SerialNumber: StrictStr
    TagKeys: list[StrictStr]
