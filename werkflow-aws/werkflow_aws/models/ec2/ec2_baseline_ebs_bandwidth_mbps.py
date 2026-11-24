from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2BaselineEbsBandwidthMbps(BaseModel):
    Min: StrictInt | None = None
    Max: StrictInt | None = None
