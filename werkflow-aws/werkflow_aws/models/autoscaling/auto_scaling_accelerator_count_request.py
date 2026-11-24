from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AutoScalingAcceleratorCountRequest(BaseModel):
    Min: StrictInt | None = None
    Max: StrictInt | None = None
