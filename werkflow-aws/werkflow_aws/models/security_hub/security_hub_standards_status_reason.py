from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubStandardsStatusReason(BaseModel):
    StatusReasonCode: StrictStr | None = None
