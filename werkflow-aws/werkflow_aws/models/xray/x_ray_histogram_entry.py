from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class XRayHistogramEntry(BaseModel):
    Value: StrictFloat | StrictInt | None = None
    Count: StrictInt | None = None
