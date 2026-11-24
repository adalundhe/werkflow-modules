from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2MediaDeviceMemoryInfo(BaseModel):
    SizeInMiB: StrictInt | None = None
