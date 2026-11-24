from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2FpgaDeviceMemoryInfo(BaseModel):
    SizeInMiB: StrictInt | None = None
