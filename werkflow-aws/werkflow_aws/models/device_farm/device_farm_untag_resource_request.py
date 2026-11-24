from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmUntagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    TagKeys: list[StrictStr]
