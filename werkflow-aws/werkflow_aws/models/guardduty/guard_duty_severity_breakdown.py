from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GuardDutySeverityBreakdown(BaseModel):
    Critical: StrictInt | None = None
    High: StrictInt | None = None
    Medium: StrictInt | None = None
    Low: StrictInt | None = None
    Info: StrictInt | None = None
