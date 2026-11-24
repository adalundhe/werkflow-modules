from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchGetUpgradeStatusRequest(BaseModel):
    DomainName: StrictStr
