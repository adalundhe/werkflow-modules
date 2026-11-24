from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_tag import DeviceFarmTag


class DeviceFarmTagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[DeviceFarmTag]
