from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2InferenceDeviceMemoryInfo(BaseModel):
    SizeInMiB: StrictInt | None = None
