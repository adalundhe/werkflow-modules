from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubStatusReason(BaseModel):
    ReasonCode: StrictStr | None = None
    Description: StrictStr | None = None
