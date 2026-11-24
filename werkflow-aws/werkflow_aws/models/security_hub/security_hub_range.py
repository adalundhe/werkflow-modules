from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubRange(BaseModel):
    Start: StrictInt | None = None
    End: StrictInt | None = None
    StartColumn: StrictInt | None = None
