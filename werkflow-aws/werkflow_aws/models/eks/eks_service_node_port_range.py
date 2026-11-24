from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EKSServiceNodePortRange(BaseModel):
    minPort: StrictInt | None = None
    maxPort: StrictInt | None = None
