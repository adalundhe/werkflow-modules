from __future__ import annotations
from pydantic import BaseModel, StrictFloat


class CloudWatchStatisticSet(BaseModel):
    SampleCount: StrictFloat | None = None
    Sum: StrictFloat | None = None
    Minimum: StrictFloat | None = None
    Maximum: StrictFloat | None = None
