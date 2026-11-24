from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubEnableSecurityHubV2Request(BaseModel):
    Tags: dict[StrictStr, StrictStr] | None = None
