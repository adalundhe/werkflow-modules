from __future__ import annotations
from pydantic import BaseModel, StrictInt


class OpenSearchInstanceCountLimits(BaseModel):
    MinimumInstanceCount: StrictInt | None = None
    MaximumInstanceCount: StrictInt | None = None
