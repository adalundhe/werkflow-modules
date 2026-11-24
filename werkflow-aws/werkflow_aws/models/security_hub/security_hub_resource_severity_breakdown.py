from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubResourceSeverityBreakdown(BaseModel):
    Other: StrictInt | None = None
    Fatal: StrictInt | None = None
    Critical: StrictInt | None = None
    High: StrictInt | None = None
    Medium: StrictInt | None = None
    Low: StrictInt | None = None
    Informational: StrictInt | None = None
    Unknown: StrictInt | None = None
