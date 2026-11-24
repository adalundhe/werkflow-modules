from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .security_hub_range import SecurityHubRange


class SecurityHubPage(BaseModel):
    PageNumber: StrictInt | None = None
    LineRange: SecurityHubRange | None = None
    OffsetRange: SecurityHubRange | None = None
