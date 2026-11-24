from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EKSServiceNodePortRangeModel(BaseModel):
    minPort: StrictInt | None = None
    maxPort: StrictInt | None = None
