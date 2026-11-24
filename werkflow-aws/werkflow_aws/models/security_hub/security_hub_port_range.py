from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubPortRange(BaseModel):
    Begin: StrictInt | None = None
    End: StrictInt | None = None
