from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubSeverityTrendsCount(BaseModel):
    Unknown: StrictInt | None = None
    Informational: StrictInt | None = None
    Low: StrictInt | None = None
    Medium: StrictInt | None = None
    High: StrictInt | None = None
    Critical: StrictInt | None = None
    Fatal: StrictInt | None = None
    Other: StrictInt | None = None
