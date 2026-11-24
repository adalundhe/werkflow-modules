from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmListTagsForResourceRequest(BaseModel):
    ResourceARN: StrictStr
