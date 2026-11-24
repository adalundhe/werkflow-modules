from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SSMSeveritySummary(BaseModel):
    CriticalCount: StrictInt | None = None
    HighCount: StrictInt | None = None
    MediumCount: StrictInt | None = None
    LowCount: StrictInt | None = None
    InformationalCount: StrictInt | None = None
    UnspecifiedCount: StrictInt | None = None
